import asyncio
import aiohttp

from snorq.logging import get_logger
from snorq.alerts import Alert


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


async def sniff(*, data: dict, alert: Alert):
    while True:
        interval = data["interval"]
        result = await fetch(data)
        # Validate against expected config here & send an email if there's any issues.
        exp_status = data["expected"]["status"]
        if result["status"] != exp_status:
            logger.error(f"Error sniffing {data['url']} with Status: {result['status']}")
            asyncio.create_task(alert.send_email(
                subject=f"Snorq - Sniffing Error",
                content=f"Snorq detected an error when matching the status code {exp_status} with the response status - {result['status']}.",
            ))
        else:
            logger.debug(f"Successfully sniffed {data['url']} - Status: {result['status']}")
        await asyncio.sleep(interval)
