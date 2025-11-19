from datetime import datetime, timedelta

def build_payload(ceremonies):
    payload = []
    for c in ceremonies:
        start = datetime.strptime(f"{c['date']} {c['time']}", "%Y-%m-%d %H:%M")
        end = start + timedelta(minutes=c["duration_minutes"])
        payload.append({
            "subject": c["name"],
            "start": {"dateTime": start.isoformat()},
            "end": {"dateTime": end.isoformat()},
            "body": c["agenda"]
        })
    return payload
