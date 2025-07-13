import json
from pathlib import Path


class Config:

    path: Path
    _data: list[dict] = None

    def __init__(self, path: str = "snorq.json"):
        self.path = Path(path)

    def load_config(self):
        if not self.path.exists():
            raise FileNotFoundError(f"Config file not found - {self.path}")
        with self.path.open("r", encoding="utf-8") as f:
            self._data = json.load(f)

    @property
    def data(self) -> list[dict]:
        return self._data
