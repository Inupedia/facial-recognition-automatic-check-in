import cv2
import streamlink
import asyncio
from .stream_recognition import StreamFaceRecognition


class TwitchStream:
    def __init__(self, channel_name):
        self.channel_name = channel_name

    async def start(self):
        streams = streamlink.streams(f"https://www.twitch.tv/{self.channel_name}")

        if "best" in streams:
            url = streams["best"].url
        elif "worst" in streams:
            url = streams["worst"].url
        else:
            raise ValueError("Could not get stream URL")

        cap = cv2.VideoCapture(url)

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


class BilibiliStream:
    def __init__(self, room_id):
        self.room_id = room_id

    async def start(self):
        streams = streamlink.streams(f"https://live.bilibili.com/{self.room_id}")

        if "best" in streams:
            url = streams["best"].url
        elif "worst" in streams:
            url = streams["worst"].url
        else:
            raise ValueError("Could not get stream URL")

        await StreamFaceRecognition(url).run_recognition()
