"""MCP tool (Camera/Microphone Connector)."""
import cv2
from utils.logger import logger
class MCPTool:
    def __init__(self, camera_index=0):
        self.cam = None
        try:
            self.cam = cv2.VideoCapture(camera_index)
        except Exception as e:
            logger.error("Failed to init camera: %s", e)
    def get_frame(self):
        if not self.cam:
            return None
        ret, frame = self.cam.read()
        if not ret:
            return None
        return frame
    def release(self):
        if self.cam:
            self.cam.release()
