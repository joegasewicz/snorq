import asyncio

from snorq.logging import get_logger
from snorq.consumer import consumer
from snorq.producer import producer
from snorq.config import Config


logger = get_logger()


async def main():
    config = Config()
    config.load_config()
    logger.debug(f"Successfully loaded config: {config.data}")
    # Create the queue
    queue = asyncio.Queue()
    # Create Producers
    await producer(queue, config.data)
    # Create Consumers
    await consumer(queue)


if __name__ == "__main__":
    logger.info("Sniffy running on http://localhost:8080")
    # Run event loop
    asyncio.run(main())
