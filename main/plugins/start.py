import requests
import random
from telethon import events, Button
from .. import bot as tcrep1

S = '/' + 's' + 't' + 'a' + 'r' + 't'
DEVELOPER_CHANNEL_LINK_1 = 'https://t.me/V_1_1_1_0'
DEVELOPER_CHANNEL_LINK_2 = 'https://t.me/l_s_I_I'
BOT_CHANNEL_LINK = 'https://t.me/tcrep1'

image_urls = [
    "https://telegra.ph/file/e87601e9b2fffde7c577f.jpg",
    "https://telegra.ph/file/fd37cfdebb69412544853.jpg",
    "https://telegra.ph/file/52f3b7ddee993a5b89092.jpg",
    "https://telegra.ph/file/fd37cfdebb69412544853.jpg",
    "https://telegra.ph/file/2786b39f4d0b807d38a7d.jpg",
    "https://telegra.ph/file/05e2f3bec3a95edc599b7.jpg"
]

@tcrep1.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    image_url = random.choice(image_urls)
    image_file = "image.jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_file, 'wb') as f:
            f.write(response.content)
    else:
        await event.reply("**حدث خطأ أثناء تنزيل الصورة.**")
        return

    await event.client.send_file(event.chat_id, image_file, caption="**أرسل لي رابط أي رسالة لاستنسخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً.**", buttons=[
        [Button.url("الدعم / المطور ²🎋", DEVELOPER_CHANNEL_LINK_1),
         Button.url("الدعم / المطور ¹🌿", DEVELOPER_CHANNEL_LINK_2)],
        [Button.url("قناة البوت", BOT_CHANNEL_LINK)]
    ])

@tcrep1.on(events.NewMessage(pattern=r"/stop"))
async def stop_process(event):
    await event.reply("**تم إيقاف العملية.**")
