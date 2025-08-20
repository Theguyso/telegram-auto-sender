# Telegram Auto Sender by Theguyso

A Python automation script that sends rotating messages to selected Telegram groups/channels at regular intervals.  
All configuration (API keys, group links, messages, delays) is managed through `config.json` for security and convenience.

---

## 🚀 Features
- Login with your **Telegram user account** (via Telethon).
- Send messages to multiple groups/channels on a schedule.
- Rotate through multiple messages in sequence.
- Configurable delays between messages and rounds.
- Logging of all sent messages and errors.

---

## 🛠 Requirements
- Python 3.8+
- [Telethon](https://github.com/LonamiWebs/Telethon)

Install dependencies:
```bash
pip install -r requirements.txt


⚙️ Configuration

Create a file named config.json in the project folder:
{
  "api_id": 123456,
  "api_hash": "abcdef123456789",
  "groups": [
    "https://t.me/mygroup1",
    "https://t.me/mygroup2"
  ],
  "messages": [
    "🔥 Promo 1: Get 1,000 followers for $1.00 only!",
    "🚀 Promo 2: Twitter followers with 30 days refill guarantee!",
    "💡 Promo 3: High-quality Twitter followers with 30 days refill guarantee!"
  ],
  "delay_between_groups": 10,
  "delay_between_rounds": 600
}

api_id & api_hash: Get from my.telegram.org

groups: List of group/channel links where messages will be sent

messages: Messages that will be rotated in order

delay_between_groups: Seconds to wait between sending to each group

delay_between_rounds: Seconds to wait before restarting the loop


▶️ Usage

Run the script:


python telegram_auto_sender.py

On first run, you’ll be asked for a login code (Telegram will send it to your account).

📜 Logs

All activity is logged to telegram_auto_sender.log:

✅ Success messages

❌ Errors




📜 License

MIT License – free to use, modify, and share.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.