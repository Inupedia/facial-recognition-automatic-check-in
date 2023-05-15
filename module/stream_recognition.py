import face_recognition
import os, sys
import cv2
import numpy as np
import math
import pickle
import asyncio


class StreamFaceRecognition:
    def __init__(self, stream_url):
        self.stream_url = stream_url

    async def run_recognition(self):
        cap = cv2.VideoCapture(self.stream_url)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            # TODO: process the frame, such as face detection, object tracking, etc.

            cv2.imshow("Twitch Stream", frame)

            if cv2.waitKey(1) == ord("q"):
                break

            await asyncio.sleep(0)

        cap.release()
        cv2.destroyAllWindows()
