"""SessionService: small in-memory session store for demo."""
import time
class SessionService:
    def __init__(self):
        self.sessions = {}
    def create_session(self, user_id):
        sid = f"sess-{int(time.time())}"
        self.sessions[sid] = {"user_id": user_id, "created": time.time()}
        return sid
    def get_session(self, sid):
        return self.sessions.get(sid)
    def update_session(self, sid, data):
        if sid in self.sessions:
            self.sessions[sid].update(data)
            return True
        return False
