"""AlertAgent: triggers alerts via Twilio or logs actions in demo mode."""
from utils.logger import logger
from tools.twilio_tool import TwilioTool
from utils.config import settings
class AlertAgent:
    def __init__(self):
        self.demo_mode = settings.get("DEMO_MODE", True)
        self.twilio = TwilioTool() if not self.demo_mode else None
        self.alert_contact = settings.get("ALERT_CONTACT")
    def trigger(self, decision):
        reason = decision.get("reason", "unspecified")
        summary = {"reason": reason, "timestamp": decision.get("timestamp"), "note": decision.get("speak_text", "")}
        if self.demo_mode:
            logger.warning(f"[DEMO] Would escalate: {summary}. Contact: {self.alert_contact}")
            return {"status": "demo_logged", "summary": summary}
        else:
            msg = f"AegisAgent Alert: {reason}. {summary['note']}"
            res = self.twilio.send_sms(self.alert_contact, msg)
            logger.info(f"Alert sent via Twilio: {res}")
            return {"status": "sent", "twilio": res}
