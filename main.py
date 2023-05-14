from module import *
import asyncio

if __name__ == "__main__":
    fr = face_recognition.FaceRecognition()
    fr.print_hello_world()

    # stream from Bilibili
    bilibili_stream = BilibiliStream("4926600")
    asyncio.run(bilibili_stream.start())



