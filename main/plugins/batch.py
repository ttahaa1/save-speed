import os
import asyncio

batch = []

@Bot.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/cancel'))
async def cancel(event):
    if not event.sender_id in batch:
        return await event.reply("**❌ لا يوجد دفعة نشطة. ❌**")
    batch.clear()
    await event.reply("**✅ تم. ✅**")

async def save_file(client, sender, link, filename):
    try:
        if not os.path.exists("/app/downloads"):
            os.makedirs("/app/downloads")
        await client.download_media(link, f"/app/downloads/{filename}")
    except Exception as e:
        await client.send_message(sender, f"فـشـل فـي الـحـفـظ: {link}\nالـخـطـأ: {e}")

@Bot.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    if event.sender_id in batch:
        return await event.reply("**❌ لقد بدأت بالفعل دفعة واحدة، انتظر حتى تكتمل يا مالك الغباء! ❌**")
    async with Bot.conversation(event.chat_id) as conv: 
        await conv.send_message("**📩 أرسل لي رابط الرسالة التي تريد بدء الحفظ منها كرد على هذه الرسالة. 📩**", buttons=Button.force_reply())
        try:
            link = await conv.get_reply()
            link = link.text
            if not link.startswith("http"):
                link = f"https://{link}"
        except Exception as e:
            print(e)
            await conv.send_message("**❌ لا يمكن الانتظار لمزيد من الوقت للرد! ❌**")
            return conv.cancel()
        try:
            filename = link.split("/")[-1]
            await save_file(client, event.sender_id, link, filename)
        except Exception as e:
            await conv.send_message(f"فـشـل فـي الـحـفـظ: {link}\nالـخـطـأ: {e}")
            return conv.cancel()
        await conv.send_message("**✅ تم بدء الحفظ. ✅**")
        batch.append(event.sender_id)

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
                await client.send_message(sender, "**✅ تم الانتهاء من الدفعة. ✅**")
                break
        except Exception as e:
            print(e)
            await client.send_message(sender, "**✅ تم الانتهاء من الدفعة. ✅**")
            break
        try:
            await get_bulk_msg(userbot, client, sender, link, i)
