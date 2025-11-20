"""Main entrypoint for AegisAgent demo."""
import argparse, time
from agents.vision_agent import VisionAgent
from agents.reasoner_agent import ReasonerAgent
from agents.alert_agent import AlertAgent
from agents.accessibility_agent import AccessibilityAgent
from utils.logger import logger
from utils.config import settings

def run_demo(loop_interval=5, duration=30):
    logger.info("Starting AegisAgent demo...")
    vision = VisionAgent()
    reasoner = ReasonerAgent()
    alert = AlertAgent()
    access = AccessibilityAgent()
    start = time.time()
    while time.time() - start < duration:
        perception = vision.run_once()
        decision = reasoner.evaluate(perception)
        if decision.get("escalate"):
            alert.trigger(decision)
        if decision.get("speak"):
            access.speak(decision.get("speak_text", "Be careful."))
        time.sleep(loop_interval)
    logger.info("Demo finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--interval", type=int, default=5)
    parser.add_argument("--duration", type=int, default=30)
    args = parser.parse_args()
    if args.demo:
        run_demo(loop_interval=args.interval, duration=args.duration)
