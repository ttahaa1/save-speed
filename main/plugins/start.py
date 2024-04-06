import os
from telethon import events, Button
from .. import bot as Drone
from ethon.mystarts import start_srb

S = '/' + 'ب' + 'د' + 'ء'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    Drone = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv:
        xx = await conv.send_message("أرسل لي أي صورة لاستخدامها كصورة مصغرة كرد على هذه الرسالة.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("لم يتم العثور على وسائط.")
            return
        mime = x.file.mime_type
        if not ('png' in mime or 'jpg' in mime or 'jpeg' in mime):
            await xx.edit("لم يتم العثور على صورة.")
            return
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'جارٍ المحاولة.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("تم حفظ الصورة المصغرة مؤقتًا!")

@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    Drone = event.client
    await event.edit('جارٍ المحاولة.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('تم الحذف!')
    except Exception:
        await event.edit("لم يتم حفظ أي صورة مصغرة.")

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "\n\nSUPPORT: @l_s_I_I  أرسل لي رابط أي رسالة لاستنساخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً."
    message = await start_srb(event, text)

    # Download and send the animated video
    await event.client.send_file(event.chat_id, "speed.mp4", force_document=True, reply_to=message)

    # Send transparent buttons below the video
    buttons = [Button.inline("Option 1", b"option1"), Button.inline("Option 2", b"option2")]
    await event.client.send_message(event.chat_id, "Choose an option:", buttons=buttons)
