"""AccessibilityAgent: TTS announcements and short dialog actions."""
from utils.logger import logger
class AccessibilityAgent:
    def __init__(self):
        pass
    def speak(self, text):
        logger.info(f"[TTS] {text}")
        print(f"[TTS] {text}")
