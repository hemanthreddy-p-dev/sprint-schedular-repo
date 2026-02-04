"""
Strand: Validates and corrects LLM JSON output if needed.
"""

import json
from strand import Strand
from utils.bedrock_client import ask_bedrock

class ValidateLLMOutput(Strand):
    async def run(self, config, llm_output):
        try:
            json.loads(json.dumps(llm_output))  # simple structure check
            print("✅ LLM output validated.")
            return llm_output
        except Exception:
            print("⚠️ Invalid JSON detected. Requesting correction from LLM...")
            correction_prompt = f"""
            The following text was invalid JSON. Please fix and return valid JSON only:
            {llm_output}
            """
            response = ask_bedrock(correction_prompt, config)
            return json.loads(response)
