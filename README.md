# Snorq

**Snorq** is an asynchronous CLI tool that monitors URLs by sniffing them at regular intervals. It's built with `asyncio` and `aiohttp` for high-concurrency performance and is ideal for uptime checks, content validation, and status monitoring.

---

## 📦 Installation

```bash
pip install snorq
```

---

## 🚀 Features

- Asynchronous URL sniffing
- Periodic sniffing with configurable intervals
- JSON-based configuration (`snorq.json`)
- Logs responses, errors, and timeouts
- Easily extendable and embeddable in other apps
