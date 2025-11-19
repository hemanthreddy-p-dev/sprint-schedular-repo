from strands.agent import Agent
import json
from prstrands.llm_planner import plan_sprint_ceremonies
from prstrands.payload_builder import build_payload
from prstrands.notifier import send_payloads


def extract_text_from_response(response):
    """Extract plain text or JSON string from various possible Strands AgentResult formats."""
    # Try common text attributes
    for field in ["output_text", "text", "content", "result", "message"]:
        if hasattr(response, field):
            return getattr(response, field)

    # Try list-based outputs
    if hasattr(response, "outputs"):
        outputs = response.outputs
        if isinstance(outputs, list) and outputs:
            first = outputs[0]
            if isinstance(first, dict) and "text" in first:
                return first["text"]
            elif hasattr(first, "text"):
                return first.text

    # If response is already a dict/list (structured JSON), return as-is
    if isinstance(response, (dict, list)):
        return json.dumps(response, indent=2)

    # Fallback: convert to string
    try:
        return str(response)
    except Exception:
        raise TypeError(f"Cannot extract text from response type: {type(response)}")


def main_run(config, user_prompt=None):
    """Main orchestration function using Strands Agent."""
    agent = Agent()

    # Get the LLM-generated response
    response = agent(user_prompt)

    # Extract the LLM text safely
    response_text = extract_text_from_response(response)

    # ✅ Ensure it's a string before slicing or printing
    if not isinstance(response_text, str):
        response_text = json.dumps(response_text, indent=2)

    print("🧠 LLM Raw Output (trimmed):")
    print(response_text[:500], "..." if len(response_text) > 500 else "")

    # Parse LLM JSON into structured ceremonies
    ceremonies = plan_sprint_ceremonies(response_text)

    # Build Power Automate payload
    payload = build_payload(ceremonies)

    # Send payload to Teams via webhook
    send_payloads(config, payload)
