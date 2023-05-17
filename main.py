from module import *
import asyncio

if __name__ == "__main__":
    # stream from Bilibili
    # 4926600 26098238 22947919
    bilibili_stream = BilibiliStream("24489698")
    asyncio.run(bilibili_stream.start())
