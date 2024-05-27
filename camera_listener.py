# camera_listener.py
import cv2

class CameraListener:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        # Attempt to set the maximum resolution
        self.set_max_resolution()

        if self.cap.isOpened():
            print("Camera initialized successfully.")
        else:
            print("Failed to initialize camera.")

    def set_max_resolution(self):
        # A list of standard resolutions to check
        resolutions = [
            (3840, 2160),  # 4K UHD
            (2560, 1440),  # QHD
            (1920, 1080),  # Full HD
            (1280, 720),  # HD
            (640, 480)  # Standard
        ]

        for width, height in resolutions:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

            actual_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            if actual_width == width and actual_height == height:
                print(f"Set resolution to {width}x{height}")
                break
        else:
            print("Failed to set a high resolution, using default settings.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
