import os, sys
import cv2
import numpy as np
import math
import pickle
import asyncio
import threading
from deepface import DeepFace


class StreamFaceRecognition:
    def __init__(self, stream_url):
        self.stream_url = stream_url
        self.process_current_frame = True
        self.metrics = ["cosine", "euclidean", "euclidean_l2"]

    def verify_face(self, frame):
        res = DeepFace.find(
            img_path=frame,
            db_path="./face_db",
            distance_metric=self.metrics[0],
        )
        print(res)

    def verify_two_images(self, frame):
        img = cv2.imread("./face_db/zhubo1.png")

        res = DeepFace.verify(frame, img)
        print(res)

    async def run_recognition(self):
        cap = cv2.VideoCapture(self.stream_url)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            # TODO: process the frame, such as face detection, object tracking, etc.
            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                self.verify_face(small_frame)
                # self.verify_two_images(small_frame)
                # save the frame
                # cv2.imwrite("./face_db/zhubo.png", frame)

            self.process_current_frame = not self.process_current_frame

            cv2.imshow("Streaming Detection", frame)

            if cv2.waitKey(1) == ord("q"):
                break

            await asyncio.sleep(0)

        cap.release()
        cv2.destroyAllWindows()

    async def run_local_stream(self):
        cap = cv2.VideoCapture(self.stream_url)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow("Streaming", frame)

            if cv2.waitKey(1) == ord("q"):
                break

            await asyncio.sleep(0)

        cap.release()
        cv2.destroyAllWindows()
