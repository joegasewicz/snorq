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
- Email alerts via SMTP (async, using aiosmtplib)

---

## 📦 Installation

```bash
pip install snorq
```
## 🛠 Usage
```
snorq --strict true
```
### CLI Options
```
--strict: Prevents duplicate URLs from being enqueued (default: true)
```
### 🧾 Configuration: snorq.json

The snorq.json file defines which domains Snorq will monitor ("sniff"), how frequently, and what conditions to check for. It also configures alerting options such as email notifications.
### 🔧 Example Configuration
```bash
{
  "alerts": {
    "email": {
      "smtp_server": "smtppro.zoho.eu",
      "port": 587,
      "username": "<EMAIL_ADDRESS>",
      "password": "<EMAIL_PASSWORD>",
      "from": "<SENDER_EMAIL>",
      "to": ["<RECIPIENT_EMAIL_1>", "<RECIPIENT_EMAIL_2>"]
    }
  },
  "domains": [
    {
      "url": "https://yahoo.com",
      "interval": 5,
      "expected": {
        "status": 200,
        "body": {
          "in": ["josef"]
        },
        "headers": {
          "content_type": "html/text"
        }
      }
    }
  ]
}
```
## 📝 Field Breakdown

### `alerts.email`

`smtp_server`: SMTP server address (e.g. smtppro.zoho.eu)

`port`: SMTP port (typically 587 for TLS)

`username`: Login username for the SMTP server

`password`: SMTP password or app-specific password

`from`: The sender address (displayed as the "from" in emails)

`to`: List of recipient email addresses for alerts

### `domains`

A list of domain targets to monitor.

Each entry supports:

`url`: The full URL to sniff

`interval`: How often to sniff (in seconds)

`expected.status`: Expected HTTP status code (e.g. 200)

`expected.body.in`: List of strings that should be present in the response body

`expected.headers.content_type`: Expected Content-Type header

## 🧪 Development
```
pipenv shell
pipenv install
snorq --strict true
```
## 📄 License

MIT License
