import requests
import os
import random
from telethon import events, Button

S = '/' + 's' + 't' + 'a' + 'r' + 't'
DEVELOPER_CHANNEL_LINK = 'https://t.me/V_1_1_1_0'  # Changed developer channel link

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    Drone = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv:
        xx = await conv.send_message("أرسل لي أي صورة لتكون الصورة المصغرة كرد على هذه الرسالة.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("لم يتم العثور على وسائط.")
        mime = x.file.mime_type
        if not ('png' in mime or 'jpg' in mime or 'jpeg' in mime):
            await xx.edit("لم يتم العثور على صورة.")
            return
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'جارٍ المحاولة...')
        media_url = await x.download_media()
        await t.edit("تم حفظ الصورة مؤقتًا!")

@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    Drone = event.client
    await event.edit('جارٍ المحاولة...')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('تم الحذف!')
    except Exception:
        await event.edit("لم يتم العثور على أي صورة مصغرة.")

# Function to fetch a random anime image URL from a Telegram channel
async def fetch_random_anime_image_url():
    from telethon.sync import TelegramClient
    # Ensure you have the necessary credentials set up to authenticate with Telegram
    api_id = 'API_ID'
    api_hash = 'API_HASH'
    client = TelegramClient('anon', api_id, api_hash)
    await client.start()
    messages = await client.get_messages('bkddgfsa', limit=50)  # Adjust limit as needed
    anime_messages = [msg for msg in messages if msg.photo]  # Filter only messages with photos
    random_anime_message = random.choice(anime_messages)
    return random_anime_message.photo

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    # Fetching a random anime image URL
    photo = await fetch_random_anime_image_url()
    if not photo:
        await event.reply("فشل في استرداد صورة الأنمي العشوائية.")
        return

    # Downloading the image
    image_file = "image.jpg"
    await event.client.download_media(photo, image_file)

    # Sending the image with the support button
    await event.client.send_file(event.chat_id, image_file, caption="** أرسل لي رابط أي رسالة لاستنساخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً. ✓ **", buttons=[
        [Button.url("الدعم / المطور", DEVELOPER_CHANNEL_LINK)]
    ])

# يمكن استخدام الأمر /stop لإيقاف العملية
@Drone.on(events.NewMessage(pattern=r"/stop"))
async def stop_process(event):
    # إلغاء عملية التحويل
    # قم بإيقاف أي عمليات تقوم بها الآن
    # قم بإرسال رسالة تؤكد إيقاف العملية للمستخدم
    await event.reply("تم إيقاف العملية. ✓")
