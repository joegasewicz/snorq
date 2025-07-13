import asyncio
import logging

from marshmallow import ValidationError

from snorq.exceptions import DuplicateURLError, DataValidationError
from snorq.schemas import DataSchema
from snorq.config import DataType


class Producer:
    """
    Producer class responsible for validating and enqueueing URL data
    into an asyncio-based task queue for sniffing.

    Attributes:
        data (list[dict]): A list of dictionaries, each containing URL configuration.
        queue (asyncio.Queue): The asyncio queue to which valid URL tasks will be added.
        strict (bool): If True, duplicate URLs raise an exception during enqueue.
        _seen_urls (set[str]): Internal set used to track already-enqueued URLs.

    Methods:
        validate_data(): Validates the data against the DataSchema.
        enqueue(): Puts validated data into the queue, enforcing duplicate checks if strict mode is enabled.
    """
    data: DataType

    queue: asyncio.Queue

    _seen_urls: set[str]

    strict: bool

    def __init__(
        self,
        *,
        queue: asyncio.Queue,
        data: DataType,
        strict: bool = True,
    ):
        self.data = data
        self.queue = queue
        self._seen_urls = set()
        self.strict = strict

    async def enqueue(self) -> None:
        """
        Enqueue validated URL data into the async queue.
        If `strict` mode is enabled, duplicate URLs will raise a DuplicateURLError.
        Otherwise, duplicates are silently ignored.

        :raises DuplicateURLError: If a duplicate URL is encountered in strict mode.
        """
        for data in self.data["domains"]:
            if not self.strict or data["url"] not in self._seen_urls:
                self._seen_urls.add(data["url"])
                await  self.queue.put(data)
            else:
                raise DuplicateURLError(f"Duplicate URL detected: {data['url']}")


    def validate_data(self) -> None:
        """
        Validate the producer data against the DataSchema definition.
        Logs successful validation, and raises DataValidationError if schema validation fails.

        :raises DataValidationError: If the provided data does not match the schema.
        """
        try:
            validated = DataSchema().load(self.data)
            logging.debug(f"Successfully validated data: {validated}")
        except ValidationError as err:
            logging.error(f"Data validation error: {err}")
            raise DataValidationError(f"Validation error: {err}")
