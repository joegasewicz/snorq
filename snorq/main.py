import asyncio

import click

from snorq.logging import get_logger
from snorq.consumer import Consumer
from snorq.producer import Producer
from snorq.config import Config
from snorq.alerts import Alert, Emailer


logger = get_logger()

async def snorq(*, strict: bool):
    config = Config(strict=strict)
    config.load_config()
    config.check_intervals()
    logger.debug(f"Successfully loaded config: {config.data}")
    # Create the queue
    queue = asyncio.Queue()
    # Create Producers
    producer = Producer(
        queue=queue,
        data=config.data,
        strict=config.strict,
    )
    producer.validate_data()
    await producer.enqueue()
    # Create Consumers
    emailer = Emailer(config=config)
    alert = Alert(emailer=emailer)
    consumer = Consumer(queue=queue, alert=alert)
    await consumer.run()


@click.command()
@click.option("--strict", default=True, help="Prevent duplicate URLs being sniffed")
def main(strict: bool):
    asyncio.run(snorq(strict=strict))


if __name__ == "__main__":
    main()
