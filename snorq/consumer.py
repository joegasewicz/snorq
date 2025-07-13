import asyncio
from asyncio import create_task

from snorq.logging import get_logger
from snorq.sniffer import sniff
from snorq.alerts import Alert


logger = get_logger()


class Consumer:

    queue: asyncio.Queue

    alert: Alert

    def __init__(self, *, queue: asyncio.Queue, alert: Alert):
        self.queue = queue
        self.alert = alert

    async def run(self):
        while True:
            data = await self.queue.get()
            try:
                async with asyncio.timeout(data["interval"]):
                    logger.debug(f"Sniffing {data['url']} every {data['interval']}s")
                    asyncio.create_task(sniff(data=data, alert=self.alert))
            except asyncio.TimeoutError:
                # Task automatically gets cancelled.
                # Don't block sending email
                asyncio.create_task(self.alert.send_email(
                    subject=f"Snorq - Timeout error sniffing {data['url']}. Request took more than {data['interval']}",
                    content=f"URL with {data['url']} failed to respond to request made with a wait time interval set to {data['interval']}.",
                ))
                logger.error(f"Timeout Error sniffing {data['url']}")
            except Exception as e:
                logger.error(f"Error sniffing {data['url']}: {e}")
            finally:
                logger.debug("Task completed")
                self.queue.task_done()
