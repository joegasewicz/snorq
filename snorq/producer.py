import asyncio

from snorq.exceptions import DuplicateURLError


class Producer:

    data: list[dict]

    queue: asyncio.Queue

    _seen_urls: set[str]

    strict: bool

    def __init__(
        self,
        *,
        queue: asyncio.Queue,
        data: list[dict],
        strict: bool = True,
    ):
        self.data = data
        self.queue = queue
        self._seen_urls = set()
        self.strict = strict

    async def enqueue(self) -> None:
        for data in self.data:
            if not self.strict or data["url"] not in self._seen_urls:
                self._seen_urls.add(data["url"])
                await  self.queue.put(data)
            else:
                raise DuplicateURLError(f"Duplicate URL detected: {data['url']}")
