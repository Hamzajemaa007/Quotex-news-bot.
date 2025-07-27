import logging
from telegram import Bot
from telegram.ext import Application, CommandHandler
import requests
import schedule
import time
import asyncio

BOT_TOKEN = "8386439594:AAHELXmMC0YleBh-BUaQHB8nz2XS_86-eb0"
CHANNEL_USERNAME = "@Quotex_news"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

async def send_message(text):
    try:
        await bot.send_message(chat_id=CHANNEL_USERNAME, text=text)
    except Exception as e:
        print("Error sending message:", e)

async def job():
    await send_message("📢 تنبيه: خبر اقتصادي هام بعد دقيقة! جهز روحك للدخول في السوق.")
    await asyncio.sleep(60)
    # Replace this part with real candle direction logic
    direction = "🔵 شراء" if time.time() % 2 == 0 else "🔴 بيع"
    await send_message(f"📊 نتيجة الخبر: الاتجاه هو {direction} (صفقة 1 دقيقة)")

async def scheduler():
    schedule.every().day.at("13:29").do(lambda: asyncio.create_task(job()))
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def main():
    await scheduler()

if __name__ == "__main__":
    asyncio.run(main())