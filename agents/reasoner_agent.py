"""ReasonerAgent: fuse perception + memory + LLM (Gemini) to decide action."""
from utils.logger import logger
from utils.config import settings
from memory.session_service import SessionService
from memory.memory_bank import MemoryBank
class ReasonerAgent:
    def __init__(self):
        self.session = SessionService()
        self.memory = MemoryBank()
        self.gemini_key = settings.get("GEMINI_API_KEY")
        self.demo_mode = settings.get("DEMO_MODE", True)
    def _call_gemini(self, prompt):
        logger.debug("Would call Gemini with prompt length: %d", len(prompt))
        return {"escalate": False, "speak": False, "explain": "simulated"}
    def _rules_based_decision(self, perception):
        vision = perception.get("vision", {})
        audio = perception.get("audio", {})
        decision = {"escalate": False, "speak": False}
        if vision.get("event") == "fall" and vision.get("confidence", 0) > 0.9:
            decision["escalate"] = True
            decision["reason"] = "fall_detected"
            decision["speak"] = True
            decision["speak_text"] = "I detected a fall. Are you conscious?"
        elif audio.get("scream") and audio.get("confidence", 0) > 0.9:
            decision["escalate"] = True
            decision["reason"] = "scream_detected"
            decision["speak"] = True
            decision["speak_text"] = "I heard a scream. Are you okay?"
        elif vision.get("event") == "near_vehicle":
            decision["speak"] = True
            decision["speak_text"] = "Caution: a vehicle is nearby."
        elif vision.get("event") == "object_obstructing_path":
            decision["speak"] = True
            decision["speak_text"] = f"Warning: {vision.get('object')} ahead."
        else:
            decision["speak"] = False
            decision["speak_text"] = ""
        return decision
    def evaluate(self, perception):
        if self.gemini_key:
            prompt = f"Perception: {perception}"
            return self._call_gemini(prompt)
        decision = self._rules_based_decision(perception)
        self.memory.add_event(perception)
        logger.info(f"Decision: {decision}")
        return decision
