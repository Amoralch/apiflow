import httpx
from datetime import datetime, timezone


async def send_webhook(url: str, event: str, payload: dict) -> bool:
      if not url:
                return False

      body = {
          "event": event,
          "timestamp": datetime.now(timezone.utc).isoformat(),
          "data": payload,
      }

    try:
              async with httpx.AsyncClient(timeout=10.0) as client:
                            resp = await client.post(url, json=body)
                            return resp.status_code < 400
    except httpx.HTTPError:
              return
