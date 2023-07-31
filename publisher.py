import cv2
from app.config.redis_config import redis_client

# Open a Video capture for your webcam.
video = cv2.VideoCapture(0)

# Resizing parameters
height = int(video.get(4) / 2)
width = int(video.get(3) / 2)

# Open a Redis connection to be used as publisher
server = redis_client;

# While video camera is on...
while video.isOpened():
    # Read a frame from the camera. Frame is a 2D array of pixels.
    ret, frame = video.read();
    if ret:
        frame = cv2.resize(frame, (width, height));

        # Publish the frame (message packet) to a channel named user_1
        server.publish("user_1", frame.tobytes());
video.release()
