import os
import random
import requests

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Constants
START_COMMAND = "/start"
STOP_COMMAND = "/stop"
BOT_CHANNEL_LINK = "https://t.me/tcrep1"
IMAGE_URLS = [
    "https://telegra.ph/file/e7ca0816f8f6733a08042.mp4"
]
TEMP_IMAGE_PATH = "image.jpg"

# Initialize the Pyrogram client
bot = Client("my_bot")

# Function to download a random image from the IMAGE_URLS list
def download_random_image():
    image_url = random.choice(IMAGE_URLS)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(TEMP_IMAGE_PATH, "wb") as f:
            f.write(response.content)
        return True
    return False

# Start command handler
@bot.on_message(filters.command([START_COMMAND]))
async def start_command(client, message):
    # Download a random image
    if download_random_image():
        # Send the image with a button linking to the bot channel
        await message.reply_photo(
            photo=TEMP_IMAGE_PATH,
            caption="**أرسل لي رابط أي رسالة لاستنسخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً.**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("قناة البوت", url=BOT_CHANNEL_LINK)]
            ])
        )
    else:
        await message.reply("حدث خطأ أثناء تنزيل الصورة.")

# Stop command handler
@bot.on_message(filters.command([STOP_COMMAND]))
async def stop_command(client, message):
    await message.reply("**تم إيقاف العملية.**")

# Start the bot
bot.run()
