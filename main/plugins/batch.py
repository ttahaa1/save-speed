import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot, AUTH
from main.plugins.pyroplug import get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait

from ethon.pyfunc import video_metadata
from ethon.telefunc import force_sub

ft = f"يجب عليك الانضمام إلى @{fs} لاستخدام هذا البوت."

batch = []

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/cancel'))
async def cancel(event):
    if not event.sender_id in batch:
        return await event.reply("لا يوجد دفعة نشطة.")
    batch.clear()
    await event.reply("تم.")

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if s == True:
        await event.reply(r)
        return       
    if event.sender_id in batch:
        return await event.reply("لقد بدأت بالفعل دفعة واحدة، انتظر حتى تكتمل يا مالك الغباء!")
    async with Drone.conversation(event.chat_id) as conv: 
        if s != True:
            await conv.send_message("أرسل لي رابط الرسالة التي تريد بدء الحفظ منها كرد على هذه الرسالة.", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
                try:
                    _link = get_link(link.text)
                except Exception:
                    await conv.send_message("لم يتم العثور على رابط.")
                    return conv.cancel()
            except Exception as e:
                print(e)
                await conv.send_message("لا يمكن الانتظار لمزيد من الوقت للرد!")
                return conv.cancel()
            await conv.send_message("أرسل لي عدد الملفات/النطاق التي تريد حفظها من الرسالة المحددة كرد على هذه الرسالة.", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                print(e)
                await conv.send_message("لا يمكن الانتظار لمزيد من الوقت للرد!")
                return conv.cancel()
            try:
                value = int(_range.text)
                if value > 100:
                    await conv.send_message("يمكنك الحصول على ما يصل إلى 100 ملف في دفعة واحدة فقط.")
                    return conv.cancel()
            except ValueError:
                await conv.send_message("يجب أن يكون النطاق عبارة عن عدد صحيح!")
                return conv.cancel()
            batch.append(event.sender_id)
            await run_batch(userbot, Bot, event.sender_id, _link, value) 
            conv.cancel()
            batch.clear()

async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try: 
            if not sender in batch:
                await client.send_message(sender, "تم الانتهاء من الدفعة.")
                break
        except Exception as e:
            print(e)
            await client.send_message(sender, "تم الانتهاء من الدفعة.")
            break
        try:
            await get_bulk_msg(userbot, client, sender, link, i) 
        except FloodWait as fw:
            if int(fw.x) > 299:
                await client.send_message(sender, "إلغاء الدفعة لأن لديك انتظار للتحكم في الفيض أكثر من 5 دقائق.")
                break
            await asyncio.sleep(fw.x + 5)
            await get_bulk_msg(userbot, client, sender, link, i)
        protection = await client.send_message(sender, f"جاري الانتظار لـ `{timer}` ثانية لتجنب الانتظارات الناتجة عن الفيض وحماية الحساب!")
        await asyncio.sleep(timer)
        await protection.delete()
