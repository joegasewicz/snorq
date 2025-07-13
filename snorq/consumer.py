import asyncio

from snorq.logging import get_logger
from snorq.sniffer import sniff


logger = get_logger()

async def consumer(queue: asyncio.Queue):
    while True:
        data = await queue.get()
        try:
            async with asyncio.timeout(data["interval"]):
                logger.debug(f"Sniffing {data['url']} every {data['interval']}s")
                asyncio.create_task(sniff(data))
        except asyncio.TimeoutError:
            # Task automatically gets cancelled.
            logger.error(f"Timeout Error sniffing {data['url']}")
        except Exception as e:
            logger.error(f"Error sniffing {data['url']}: {e}")
        finally:
            logger.debug("Task completed")
            queue.task_done()
