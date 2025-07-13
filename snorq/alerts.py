import asyncio

from email.message import EmailMessage
from aiosmtplib import send, SMTPResponse

from snorq.config import Config
from snorq.logging import get_logger
from snorq.exceptions import AlertEmailError


logger = get_logger()


class Emailer:

    config: Config
    _from: str
    _to: list[str]
    _smtp_server: str
    _port: int
    _start_tls: bool = True
    _username: str
    _password: str

    def __init__(self, config: Config):
        self.config = config
        self._from = self.config.email_options.email_from
        self._to = self.config.email_options.to
        self._smtp_server = self.config.email_options.smtp_server
        self._port = self.config.email_options.port
        self._start_tls = self.config.email_options.start_tls
        self._username = self.config.email_options.username
        self._password = self.config.email_options.password

    async def send_email(self, *, subject: str, content: str):
        message = EmailMessage()
        message["From"] = self._from
        message["To"] = self._to
        message["Subject"] = subject
        message.set_content(content)
        return await send(
            message,
            hostname=self._smtp_server,
            port=self._port,
            start_tls=self._start_tls,
            username=self._username,
            password=self._password,
        )


class Alert:

    emailer: Emailer

    def __init__(self, emailer: Emailer):
        self.emailer = emailer

    async def send_email(self, *, subject: str, content: str):
        resp, message = await self.emailer.send_email(subject=subject, content=content)
