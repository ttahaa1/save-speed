import requests
import random
import os
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

@tcrep1.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with tcrep1.conversation(event.chat_id) as conv:
        xx = await conv.send_message("**أرسل لي صورة لتكون الصورة المصغرة.**")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("**لم يتم العثور على وسائط.**")
            return
        mime = x.file.mime_type
        if not ('png' in mime or 'jpg' in mime or 'jpeg' in mime):
            await xx.edit("**لم يتم العثور على صورة.**")
            return
        await xx.delete()
        t = await event.client.send_message(event.chat_id, '**جارٍ المحاولة...**')
        media_url = await x.download_media()
        await t.edit("**تم حفظ الصورة مؤقتًا!**")

@tcrep1.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    await event.edit('**جارٍ المحاولة...**')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('**تم الحذف!**')
    except Exception:
        await event.edit("**لم يتم العثور على أي صورة مصغرة.**")

@tcrep1.on(events.NewMessage(pattern=r"/start"))
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

    await event.reply("**أرسل لي رابط أي رسالة لاستنسخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً.**", buttons=[
        [Button.url("إضافة صورة مصغرة 📷", "tg://msg_button?url=reply_to_message&text=set")],
        [Button.url("حذف الصورة المصغرة ❌", "tg://msg_button?url=reply_to_message&text=rem")],
        [Button.url("الدعم / المطور ²🎋", DEVELOPER_CHANNEL_LINK_1),
         Button.url("الدعم / المطور ¹🌿", DEVELOPER_CHANNEL_LINK_2)],
        [Button.url("قناة البوت", BOT_CHANNEL_LINK)]
    ])
