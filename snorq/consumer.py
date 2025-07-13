import asyncio

from snorq.logging import get_logger
from snorq.sniffer import sniff


logger = get_logger()

async def consumer(queue: asyncio.Queue):
    while True:
        url_data = await queue.get()
        try:
            async with asyncio.timeout(10):
                asyncio.create_task(sniff(url_data))
        except asyncio.TimeoutError:
            # Task automatically gets cancelled.
            logger.error(f"Timeout Error sniffing {url_data['url']}")
        except Exception as e:
            logger.error(f"Error sniffing {url_data['url']}: {e}")
        finally:
            logger.debug("Task completed")
            queue.task_done()
