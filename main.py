from module import *
import asyncio

if __name__ == "__main__":
    # stream from Bilibili
    bilibili_stream = BilibiliStream("4926600")
    asyncio.run(bilibili_stream.start())
