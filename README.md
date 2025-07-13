# Snorq

**Snorq** is an asynchronous CLI tool that monitors and sniffs URLs at scheduled intervals. It supports duplicate URL detection, retry logic, and expected content validation — perfect for building your own uptime, content, or status monitoring system.

---

## 🚀 Features

- Asynchronous URL sniffing using `aiohttp` and `asyncio`
- Recurring sniffing based on configurable intervals
- Schema validation using Marshmallow
- Duplicate URL prevention (`--strict`)
- Retry support with `max_retries`
- Logging with colorized output

---

## 📦 Installation

```bash
pip install snorq
```
🛠 Usage
```
snorq --strict true
```
CLI Options
```
--strict: Prevents duplicate URLs from being enqueued (default: true)
```
🧾 Configuration: snorq.json

This file defines what URLs to sniff and how they should behave.
```
[
  {
    "url": "https://josef.digital",
    "interval": 10,
    "max_retries": 3,
    "expected": {
      "status": 200,
      "body": {
        "in": ["josef"]
      },
      "headers": {
        "content_type": "html/text"
      }
    }
  },
  ...
]
```
🧪 Development
```
pipenv shell
pipenv install
snorq --strict true
```
📄 License

MIT License
