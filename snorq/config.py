import json
from pathlib import Path

from snorq.schemas import DataSchema

from snorq.logging import get_logger
from snorq.exceptions import ConfigEmailError


DataType = dict[str, dict]
logger = get_logger()


class EmailOptions:
    email_from: str
    to: list[str]
    smtp_server: str
    port: int
    start_tls: bool
    username: str
    password: str

    def __init__(
        self,
        *,
        email_from: str,
        to: list[str],
        smtp_server: str,
        port: int,
        start_tls: bool = True,
        username: str,
        password: str,
    ):
        self.email_from = email_from
        self.to = to
        self.smtp_server = smtp_server
        self.port = port
        self.start_tls = start_tls
        self.username = username
        self.password = password


class Config:

    path: Path
    _data: DataType
    strict: bool
    email_options: EmailOptions = None

    def __init__(
            self,
            *,
            path: str = "snorq.json",
            strict: bool = True,
    ):
        self.path = Path(path)
        self.strict = strict

    def load_config(self):
        if not self.path.exists():
            logger.error(f"Config file not found - {self.path}")
            raise FileNotFoundError(f"Config file not found - {self.path}")
        with self.path.open("r", encoding="utf-8") as f:
            self._data = json.load(f)
            if "alerts" in self._data and "email" in self._data["alerts"]:
                email_data = self._data["alerts"]["email"]
                try:
                    self.email_options = EmailOptions(
                        email_from=email_data["from"],
                        to=email_data["to"],
                        smtp_server=email_data["smtp_server"],
                        port=email_data["port"],
                        username=email_data["username"],
                        password=email_data["password"],
                        start_tls=email_data.get("start_tls"),
                    )
                except KeyError:
                    logger.error("Error reading email config from snorq.json")
                    raise ConfigEmailError("Error reading email config values from snorq.json")

    @property
    def data(self) -> DataType:
        return self._data

    def check_intervals(self):
        for d in self._data["domains"]:
            hour = 60 * 60
            interval = d["interval"]
            if interval < hour and "email" in self._data["alerts"]:
                logger.warning(f"Your interval is set to less than 1 hour for {d['url']}! You may receive a lot of emails!")

