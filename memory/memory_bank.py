"""MemoryBank: long-term event storage using Redis or in-memory fallback."""
import time, json
from utils.logger import logger
from utils.config import settings
try:
    import redis
    _redis = redis.from_url(settings.get("REDIS_URL"))
except Exception:
    _redis = None
class MemoryBank:
    def __init__(self):
        self.redis = _redis
        self.local = []
    def add_event(self, event):
        event['ts'] = time.time()
        if self.redis:
            key = f"events:{int(event['ts'])}"
            _redis.set(key, json.dumps(event))
            logger.debug("Saved event to redis key=%s", key)
        else:
            self.local.append(event)
            logger.debug("Saved event to local memory (len=%d)", len(self.local))
    def recent_events(self, n=10):
        if self.redis:
            keys = _redis.keys("events:*")[-n:]
            return [json.loads(_redis.get(k)) for k in keys]
        else:
            return self.local[-n:]
