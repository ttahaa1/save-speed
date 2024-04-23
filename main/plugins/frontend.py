import time, os

from .. import bot as Drone
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join

from telethon import events
from pyrogram.errors import FloodWait

from ethon.telefunc import force_sub

ft = f"**✨ يجب عليك الانضمام إلى @{fs} لاستخدام هذا البوت. ✨**"

message = "**📩 أرسل لي رابط الرسالة التي تريد بدء الحفظ منها كرد على هذه الرسالة. 📩**"

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply("**🔄 جاري المعالجة! 🔄**")
    try:
        if 't.me/+' in link:
            q = await join(userbot, link)
            await edit.edit(q)
            return
        if 't.me/' in link:
            await get_msg(userbot, Bot, Drone, event.sender_id, edit.id, link, 0)
    except FloodWait as fw:
        return await event.reply(f"**⏳ حاول مرة أخرى بعد {fw.x} ثانية بسبب انتظار التحكم في الفيض من تليجرام. ⏳**")
    except Exception as e:
        print(e)
        await event.reply(f"**❌ حدث خطأ أثناء عملية الاستنساخ من `{link}`\n\nالخطأ:** {str(e)} ❌**")
