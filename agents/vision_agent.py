"""VisionAgent: lightweight perception loop."""
import random, time
from utils.logger import logger
class VisionAgent:
    def __init__(self, model_path=None):
        self.demo_mode = True
    def capture_frame(self):
        logger.debug("Capturing synthetic frame...")
        return {"frame_id": int(time.time())}
    def analyze_audio(self):
        prob_scream = random.random()
        if prob_scream > 0.95:
            return {"scream": True, "confidence": prob_scream}
        return {"scream": False, "confidence": prob_scream}
    def analyze_image(self, frame):
        r = random.random()
        if r > 0.97:
            return {"event": "fall", "confidence": r}
        if r > 0.9:
            return {"event": "near_vehicle", "confidence": r}
        if r > 0.6:
            return {"event": "object_obstructing_path", "object": "chair", "confidence": r}
        return {"event": "normal", "confidence": r}
    def run_once(self):
        frame = self.capture_frame()
        audio = self.analyze_audio()
        image = self.analyze_image(frame)
        perception = {"timestamp": time.time(), "frame": frame, "audio": audio, "vision": image}
        logger.info(f"Perception: {perception}")
        return perception
