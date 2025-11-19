import requests
import json

def send_payloads(config, payload):
    webhook_url = config.get("webhook_url")
    if "YOUR_POWER_AUTOMATE_WEBHOOK_URL" in webhook_url:
        print("⚠️ Webhook not configured. Payload preview:")
        print(json.dumps(payload, indent=2))
        return

    for item in payload:
        print(f"📤 Sending {item['subject']} …")
        response = requests.post(webhook_url, json=item)
        print(f"Response {response.status_code}: {response.text}")
