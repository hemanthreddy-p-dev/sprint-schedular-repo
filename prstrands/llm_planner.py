import json
import re

def plan_sprint_ceremonies(agent_response_text):
    """
    Cleans up and parses LLM response text into structured JSON list of ceremonies.
    Handles cases where JSON is inside markdown or prefixed with \n or role wrappers.
    """
    if not isinstance(agent_response_text, str):
        raise TypeError(f"Expected str, got {type(agent_response_text)}")

    # 🧹 Step 1: Extract JSON block inside ```json ... ``` if present
    json_match = re.search(r"```json\s*(.*?)\s*```", agent_response_text, re.DOTALL)
    if json_match:
        cleaned = json_match.group(1)
    else:
        cleaned = agent_response_text

    # 🧹 Step 2: Remove assistant wrappers or metadata
    cleaned = re.sub(r'^{\s*"role":.*?"content":.*?"text":', '', cleaned, flags=re.DOTALL)
    cleaned = cleaned.replace("```", "").strip()

    # 🧹 Step 3: Extract JSON array (in case extra text surrounds it)
    array_match = re.search(r"\[\s*{.*}\s*\]", cleaned, re.DOTALL)
    if array_match:
        cleaned = array_match.group(0)

    # 🧹 Step 4: Convert literal escape sequences like "\n" → actual newlines
    cleaned = cleaned.encode("utf-8").decode("unicode_escape").strip()

    # ✅ Step 5: Try parsing as JSON
    try:
        ceremonies = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("⚠️ DEBUG: Cleaned text before parsing:\n", cleaned[:500])
        raise ValueError("LLM did not return valid JSON.") from e

    # 🧩 Step 6: Validate structure
    if not isinstance(ceremonies, list) or not all(isinstance(c, dict) for c in ceremonies):
        raise TypeError("Expected a list of ceremony dicts from the LLM output")

    return ceremonies
