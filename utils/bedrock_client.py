"""
AWS Bedrock client for structured LLM interaction.
"""

import boto3
import json
import os
from dotenv import load_dotenv

def get_bedrock_client(config=None):
    """
    Initialize AWS Bedrock runtime client using .env credentials.
    Supports session tokens for temporary IAM credentials.
    """
    load_dotenv()

    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_session_token = os.getenv("AWS_SESSION_TOKEN")  # ✅ optional token
    region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

    session_args = {
        "region_name": region
    }

    if aws_access_key and aws_secret_key:
        session_args["aws_access_key_id"] = aws_access_key
        session_args["aws_secret_access_key"] = aws_secret_key

        if aws_session_token:
            session_args["aws_session_token"] = aws_session_token

    # Initialize the Bedrock runtime client
    client = boto3.client("bedrock-runtime", **session_args)
    return client


def ask_bedrock(prompt, config=None):
    """
    Send a text prompt to AWS Bedrock (Claude 3) and return response text.
    """
    client = get_bedrock_client(config)

    body = json.dumps({
        "inputText": prompt
    })

    print("🧠 Invoking AWS Bedrock LLM...")
    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body=body
    )

    # Decode and return response
    result = response["body"].read().decode("utf-8").strip()
    return result
