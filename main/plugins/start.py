import requests
import random
from telethon import events, Button
from telethon.tl.functions.messages import GetHistoryRequest

# Replace 'bot' with your actual bot instance
bot = 'BOT_TOKEN'

S = '/' + 's' + 't' + 'a' + 'r' + 't'
DEVELOPER_CHANNEL_LINK = 'https://t.me/l_s_I_I'
DEVELOPER_CHANNEL_LINK_2 = 'https://t.me/V_1_1_1_0'

@bot.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with bot.conversation(event.chat_id) as conv:
        xx = await conv.send_message("أرسل لي أي صورة لتكون الصورة المصغرة كرد على هذه الرسالة.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("لم يتم العثور على وسائط.")
        mime = x.file.mime_type
        if not ('png' in mime or 'jpg' in mime or 'jpeg' in mime):
            await xx.edit("لم يتم العثور على صورة.")
            return
        await xx.delete()
        t = await bot.send_message(event.chat_id, 'جارٍ المحاولة...')
        media_url = await x.download_media()
        await t.edit("تم حفظ الصورة مؤقتًا!")

@bot.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    await event.edit('جارٍ المحاولة...')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('تم الحذف!')
    except Exception:
        await event.edit("لم يتم العثور على أي صورة مصغرة.")

@bot.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    # جلب صورة عشوائية من القناة
    random_number = random.randint(33, 82)
    photo_url = f'https://t.me/bkddgfsa/{random_number}'
    # إرسال الصورة مع الزرارين
    await bot.send_photo(event.chat_id, photo=photo_url, caption="**  أرسل لي رابط أي رسالة لاستنسخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً. ✓ **", buttons=[
        [Button.url("¹الدعم / المطور", DEVELOPER_CHANNEL_LINK), Button.url("الدعم / المطور ²", DEVELOPER_CHANNEL_LINK_2)]
    ])

# يمكن استخدام الأمر /stop لإيقاف العملية
@bot.on(events.NewMessage(pattern=r"/stop"))
async def stop_process(event):
    # قم بإيقاف أي عمليات تقوم بها الآن
    await event.reply("تم إيقاف العملية. ✓")
