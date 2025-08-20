# 🚀 Telegram Auto Sender by theguyso

A Python automation script using [Telethon](https://github.com/LonamiWebs/Telethon) that sends scheduled messages into selected Telegram groups or channels every 10 minutes.  
Supports rotating messages, delays between groups, and logging to file.  

---

## ✨ Features
- ✅ Sends messages as your user account (not a bot).  
- ✅ Rotates through multiple messages in order (1 → 2 → 3 → repeat).  
- ✅ Configurable delay between groups (default: 10 seconds).  
- ✅ Configurable delay between rounds (default: 10 minutes).  
- ✅ Logging to telegram_auto_sender.log for full history.  

---

## 📦 Requirements
- Python 3.8+  
- Telethon  

Install dependencies:
```bash
pip install -r requirements.txt

⚙️ Setup
 1. Get your API_ID and API_HASH from my.telegram.org. (https://my.telegram.org/)
 2. Open telegram_auto_sender.py and update:

 API_ID = 123456        # your real api_id
API_HASH = "abcdef123" # your real api_hash

3. Update your target groups and messages:

TARGET_GROUPS = [
    "https://t.me/yourgroup1",
    "https://t.me/yourgroup2"
]

MESSAGES = [
    """🔥 Promo 1: Get 1,000 followers for $1.00 only!""",
    """🚀 Promo 2: Twitter followers with 30 days refill guarantee!"""
]

4. Run the script:
python telegram_auto_sender.py

⏱️ Timing

You can change delays easily in the script:

DELAY_BETWEEN_GROUPS = 10   # seconds between each group
DELAY_BETWEEN_ROUNDS = 600  # seconds between rounds (10 minutes)

📜 License

MIT License – free to use, modify, and share.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.