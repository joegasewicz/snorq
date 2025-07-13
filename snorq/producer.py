import asyncio


async def producer(queue: asyncio.Queue, data):
    # Create Producers
    for url_data in data:
        await queue.put(url_data)
