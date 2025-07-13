import asyncio
import aiohttp

from snorq.logging import get_logger


logger = get_logger()


async def fetch(url_data: dict):
    async with aiohttp.ClientSession() as session:
        url = url_data["url"]
        async with session.get(url) as response:
            status = response.status
            body = await response.text()
            data = {
                "status": status,
                "body": body,
            }
            return data


async def sniff(url_data: dict):
    if "interval" in url_data:
        interval = url_data["interval"]
        while True:
            result = await fetch(url_data)
            logger.debug(f"Successfully sniffed {url_data['url']} - Status: {result['status']}")
            await asyncio.sleep(interval)
    else:
        result = await fetch(url_data)
        logger.debug(f"Successfully sniffed {url_data['url']} - Status: {result['status']}")
