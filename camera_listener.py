import cv2

class CameraListener:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise ValueError("Camera not accessible")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise ValueError("Failed to capture image")
        return frame

    def release(self):
        self.cap.release()

    def __del__(self):
        self.release()
