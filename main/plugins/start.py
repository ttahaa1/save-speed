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
        xx = await conv.send_message("** أرسـل لـي صـورة لـتـكـون الـصـورة المـصـغـرة. **")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("** لـم يـتـم الـعـثـور عـلى وسـائـط. **")
            return
        mime = x.file.mime_type
        if not ('png' in mime or 'jpg' in mime or 'jpeg' in mime):
            await xx.edit("** لـم يـتـم الـعـثـور عـلى صـورة. **")
            return
        await xx.delete()
        t = await event.client.send_message(event.chat_id, '** جـارٍ المـحـاولـة... **')
        media_url = await x.download_media()
        await t.edit("** تـم حـفـظ الـصـورة مـؤقـتًا! **")

@tcrep1.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    await event.edit('** جـارٍ المـحـاولـة... **')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('** تـم الـحـذف! **')
    except Exception:
        await event.edit("** لـم يـتـم الـعـثـور عـلى أي صـورة مـصـغـرة. **")

@tcrep1.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    image_url = random.choice(image_urls)
    image_file = "image.jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_file, 'wb') as f:
            f.write(response.content)
    else:
        await event.reply("** حـدث خـطأ أثـناء تـنزيل الـصـورة. **")
        return

    await event.client.send_file(event.chat_id, image_file, caption="** أرسـل لـي رابـط أي رسـالة لـاستنسخها هـنـا. بالـنـسـبـة للـرسـائل الـخـاصـة بالـقـنـاة، أرسـل رابـط الـدعـوة أولـاً. **", buttons=[
        [Button.url("** إضافة صورة مصغرة 📷 **", "tg://msg_button?url=reply_to_message&text=add")],
        [Button.url("** حذف الصورة المصغرة ❌ **", "tg://msg_button?url=reply_to_message&text=remove")],
        [Button.url("** الـدعـم / المـطـور ¹🎋 **", DEVELOPER_CHANNEL_LINK_1),
         Button.url("** الـدعـم / المـطـور ²🌿 **", DEVELOPER_CHANNEL_LINK_2)],
        [Button.url("** قـنـاة الـبـوت **", BOT_CHANNEL_LINK)]
    ])

@tcrep1.on(events.NewMessage(pattern=r"/stop"))
async def stop_process(event):
    await event.reply("** تـم إيـقـاف الـعـمـلـيـة. **")
