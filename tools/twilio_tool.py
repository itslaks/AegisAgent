"""Twilio wrapper. Requires TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN and TWILIO_FROM_NUMBER in config.py"""
from twilio.rest import Client
from utils.logger import logger
from utils.config import settings
class TwilioTool:
    def __init__(self):
        sid = settings.get("TWILIO_ACCOUNT_SID")
        token = settings.get("TWILIO_AUTH_TOKEN")
        self.from_number = settings.get("TWILIO_FROM_NUMBER")
        if not sid or not token:
            raise ValueError("Twilio credentials missing in config.")
        self.client = Client(sid, token)
    def send_sms(self, to_number, message):
        msg = self.client.messages.create(body=message, from_=self.from_number, to=to_number)
        logger.info("Twilio message sid=%s", msg.sid)
        return {"sid": msg.sid, "status": msg.status}
