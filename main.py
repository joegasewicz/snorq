import asyncio

import click

from snorq.logging import get_logger
from snorq.consumer import consumer
from snorq.producer import Producer
from snorq.config import Config


logger = get_logger()


async def snorq(*, strict: bool):
    config = Config(strict=strict)
    config.load_config()
    logger.debug(f"Successfully loaded config: {config.data}")
    # Create the queue
    queue = asyncio.Queue()
    # Create Producers
    producer = Producer(
        queue=queue,
        data=config.data,
        strict=config.strict,
    )
    await producer.enqueue()
    # Create Consumers
    await consumer(queue)


@click.command()
@click.option("--strict", default=True, help="Prevent duplicate URLs being sniffed")
def main(strict: bool):
    asyncio.run(snorq(strict=strict))


if __name__ == "__main__":
    main()
