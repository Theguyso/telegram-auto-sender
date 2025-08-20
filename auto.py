# file: telegram_auto_sender.py
import asyncio
import logging
from datetime import datetime
from telethon import TelegramClient

API_ID = 29430400  # replace with your api_id
API_HASH = "ade8afa4d0b7f1853da990d8d375dd55"  # replace with your api_hash

# Timing settings (in seconds)
DELAY_BETWEEN_GROUPS = 15      # wait 10s between sending to each group
DELAY_BETWEEN_ROUNDS = 600     # wait 10min between each round of messages

logging.basicConfig(
    filename="telegram_auto_sender.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

client = TelegramClient("session_name", API_ID, API_HASH)

TARGET_GROUPS = [
    "https://t.me/promomasterstr",
    "https://t.me/Bitcoin_Ghana_group",
    "https://t.me/smmpanelnetwork",
    "https://t.me/smmpanels2",
    "https://t.me/booksmm3",
    "https://t.me/smmpanelgrup",
    "https://t.me/ghanamart1",
    "https://t.me/GhanaAdvertsGroup",
    "https://t.me/smmdynamics",
    "https://t.me/smmmarketings",
    "https://t.me/smmpanelproviderads",
    "https://t.me/join_for_free_smmpanel_scripts",
   "https://t.me/SUB4SUB_GROUPS",
   "https://t.me/free_promotion_group11",
   "https://t.me/youtube_service_group",
   "https://t.me/FreeAdvertisingClub",
   "https://t.me/smmpromotion2",
   "https://t.me/freepromotionsgroups",
   "https://t.me/hyped_teensgh",
   "https://t.me/asteachingghanagroup",
   "https://t.me/smmowners",
   "https://t.me/booksmm3",
   "https://t.me/Royalinvestorz",





]

MESSAGES = [
    """*Twitter Followers [ Best Services 💫 ]

6852 - Twitter Followers [ Max 100K ] | 100% Real Profiles | Low Drop | No Refill ⚠️ | Instant Start | Day 100K → $3.50

6853 - Twitter Followers [ Max 100K ] | 100% Real Profiles | Low Drop | 15 Days ♻️ | Instant Start | Day 100K → $4.00

6854 - Twitter Followers [ Max 100K ] | 100% Real Profiles | Low Drop | 30 Days ♻️ | Instant Start | Day 100K → $4.60

High Bonus Rates 🔥 : 100$ %3 Bonus | 500$ %5 Bonus | 1.000$ %6 Bonus | 5.000$ %7 Bonus | 12.000$ %10 Bonus

https://verifysmm.com

Wa.me/+233551112279""",
"""🚀 Boost Your Instagram with 1,000 Followers for Just 23¢ ! 🚀

❓ Why Choose Us?

⭐️ Affordable Pricing: Just 1$ for 1,000 followers!
🔝 Top Quality: Non-Drop Followers
⚡️ Quick Delivery: Average Order takes 0-6 Hours!
🛡 Boost Your Credibility: A larger follower count attracts more interest and trust.

✨ Special Offer: First-time customers get 15% Discount on Their first order by using the code "legitbooster"

📈 How It Works:

🌐 Headover to legitbooster.com

1. 🛒 Place Your Order: Select your desired service and make a payment.
2. 📲Share Your Instagram Profile: Provide your Instagram profile link.
3. 🎉 Watch Your Account Grow: Sit back and see your follower count increase!

Mobile Money Enabled ✅

🙋‍♂️ Need Help?
📲 Wa.me/+233551112279""",
"""Instagram Followers [ Recommended ✨ ] [ Working During Updates ] ᴺᴱᵂ

181 - Instagram Followers [ Max 10M ] | %100 Old Accounts | Instant Start | Cancel Enable | No Refill ⚠️ | Speed: 100K/Day 🚀 - $1.42 per 1000

182 - Instagram Followers [ Max 10M ] | %100 Old Accounts | Instant Start | Cancel Enable | 30 Days ♻️ | Speed: 100K/Day 🚀 - $1.50 per 1000

183 - Instagram Followers [ Max 10M ] | %100 Old Accounts | Instant Start | Cancel Enable | 60 Days ♻️ | Speed: 100K/Day 🚀 - $2.24 per 1000

184 - Instagram Followers [ Max 10M ] | %100 Old Accounts | Instant Start | Cancel Enable | 90 Days ♻️ | Speed: 100K/Day 🚀 - $2.75 per 1000

185 - Instagram Followers [ Max 10M ] | %100 Old Accounts | Instant Start | Cancel Enable | 365 Days ♻️ | Speed: 100K/Day 🚀 - $3.30 per 1000

186 - Instagram Followers [ Max 10M ] | %100 Old Accounts | Instant Start | Cancel Enable | Lifetime ♻️ | Speed: 100K/Day 🚀 - $3.95 per 1000

Bonuses:

5.5% Auto Bonus On ALL Payments — Even $1

Dive Into The BONUS RUSH:

$1,000 = 6% ⚡️ $3,000 = 7% ⚡️ $5,000 = 8% ⚡️ $12,000 = 10% ⚡️ $50,000 = 15% 💎

🤝 Connect With Us 
— 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 : https://t.me/legitboostersmm
— 𝗪𝗲𝗯𝘀𝗶𝘁e: https://VERIFYSMM.COM"""

]



message_index = 0

async def send_periodic_messages():
    global message_index
    while True:
        message = MESSAGES[message_index]
        logging.info(f"Sending message: {message[:50]}...")

        for group in TARGET_GROUPS:
            try:
                await client.send_message(group, message)
                logging.info(f"✅ Sent to {group}")
            except Exception as e:
                logging.error(f"❌ Failed to send to {group}: {e}")

            await asyncio.sleep(DELAY_BETWEEN_GROUPS)

        message_index = (message_index + 1) % len(MESSAGES)

        await asyncio.sleep(DELAY_BETWEEN_ROUNDS)

async def main():
    await client.start()
    logging.info("Client started")
    await send_periodic_messages()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())