# telegram_auto_sender.pimport json
import time
import logging
from itertools import cycle
from telethon import TelegramClient

# Load config.json
with open("config.json", "r") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
PHONE_NUMBER = config["phone_number"]
TARGET_GROUPS = config["groups"]
MESSAGES = config["messages"]
DELAY_BETWEEN_GROUPS = config.get("delay_between_groups", 10)
DELAY_BETWEEN_ROUNDS = config.get("delay_between_rounds", 600)

# Setup logging
logging.basicConfig(
    filename="telegram_auto_sender.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

client = TelegramClient("session_name", API_ID, API_HASH)

async def send_messages():
    message_cycle = cycle(MESSAGES)

    while True:
        for group in TARGET_GROUPS:
            try:
                message = next(message_cycle)
                await client.send_message(group, message)
                logging.info(f"Sent to {group}: {message[:50]}...")
                print(f"✅ Sent to {group}")
                time.sleep(DELAY_BETWEEN_GROUPS)
            except Exception as e:
                logging.error(f"Failed to send to {group}: {e}")
                print(f"❌ Error sending to {group}: {e}")

        print(f"⏳ Waiting {DELAY_BETWEEN_ROUNDS} seconds before next round...")
        time.sleep(DELAY_BETWEEN_ROUNDS)

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(send_messages())