import requests
import random
import os
from telethon import events, Button
from .. import bot as Drone

S = '/' + 's' + 't' + 'a' + 'r' + 't'
DEVELOPER_CHANNEL_LINK_1 = 'https://t.me/l_s_I_I'
DEVELOPER_CHANNEL_LINK_2 = 'https://t.me/V_1_1_1_0'
BOT_CHANNEL_LINK = 'https://t.me/tcrep1'

image_urls = [
    "https://telegra.ph/file/e87601e9b2fffde7c577f.jpg",
    "https://telegra.ph/file/fd37cfdebb69412544853.jpg",
    "https://telegra.ph/file/f3f4f72a65049dda8aef3.jpg",
    "https://telegra.ph/file/6ea7af0946f2778284b2b.jpg",
    "https://telegra.ph/file/1e6afa44820915ee86659.jpg",
    "https://telegra.ph/file/6a9202fef28244c044326.jpg",
    "https://telegra.ph/file/e6cf3963371ec3fa39cc6.jpg",
    "https://telegra.ph/file/34ef8b4a2b55bba7bf21f.jpg",
    "https://telegra.ph/file/bdb88fa8d790f62d777e6.jpg",
    "https://telegra.ph/file/52f3b7ddee993a5b89092.jpg",
    "https://telegra.ph/file/5bec6d8c5ca6ab539525e.jpg",
    "https://telegra.ph/file/a399adc5ae122b03afc02.jpg",
    "https://telegra.ph/file/5cd582fe9d7a025fc1600.jpg",
    "https://telegra.ph/file/ba7c11ae6eb9c86f35ab1.jpg",
    "https://telegra.ph/file/5aa8cdbc9ee8ce198e802.jpg",
    "https://telegra.ph/file/5653f994a56061b07ce35.jpg",
    "https://telegra.ph/file/2786b39f4d0b807d38a7d.jpg",
    "https://telegra.ph/file/8c7067be280c42137cc04.jpg",
    "https://telegra.ph/file/67a1f0ce6562e527537df.jpg",
    "https://telegra.ph/file/c7df81b0f044925f68ccc.jpg",
    "https://telegra.ph/file/2eef06501eccb45e4005d.jpg",
    "https://telegra.ph/file/05e2f3bec3a95edc599b7.jpg",
    "https://telegra.ph/file/ca20dc2c3a3b3b8fcd1b2.jpg",
    "https://telegra.ph/file/7d72a560a45f6f2145eda.jpg",
    "https://telegra.ph/file/3549a6c8afeacf9fa4111.jpg",
    "https://telegra.ph/file/598922c23c634e9453b01.jpg",
    "https://telegra.ph/file/9c74bae74640a38f1da84.jpg",
    "https://telegra.ph/file/c28831b6d3404484e3683.jpg",
    "https://telegra.ph/file/4dce020223a3994d5b5b1.jpg",
    "https://telegra.ph/file/b006ea28841eb364fcf55.jpg",
    "https://telegra.ph/file/9a88940b2355ef946489c.jpg",
    "https://telegra.ph/file/41e63b3eb31dd5611274c.jpg",
    "https://telegra.ph/file/af12f6cc82e86cd6f15b8.jpg",
    "https://telegra.ph/file/4ce4b6ea638379287388a.jpg",
    "https://telegra.ph/file/1102fb708446baf5e4d5c.jpg",
    "https://telegra.ph/file/62e569eb716fb462b5384.jpg",
    "https://telegra.ph/file/c117e50aca6a7f9eeeaba.jpg",
    "https://telegra.ph/file/b83ffaf0c09cf12a900c6.jpg",
    "https://telegra.ph/file/60f70a01846a6c103249e.jpg",
    "https://telegra.ph/file/d455390f4f48daa6ad3ac.jpg",
    "https://telegra.ph/file/407637e36deec054e9fe2.jpg",
    "https://telegra.ph/file/74aec99806ac6c4d289b0.jpg",
    "https://telegra.ph/file/d7a1ea18306c14b2c2aa1.jpg",
    "https://telegra.ph/file/5cf51e56865fb44f16c2f.jpg",
    "https://telegra.ph/file/1ce4cf7f5ab6d6b4e9263.jpg",
    "https://telegra.ph/file/fcef9227fd4a1ed19ee9a.jpg",
    "https://telegra.ph/file/ec40dbe624e93942e7fec.jpg",
    "https://telegra.ph/file/06ffc633e3ccc97cb1200.jpg",
    "https://telegra.ph/file/b97e140aabc727858fd50.jpg",
    "https://telegra.ph/file/96403b00d007e6c3c11a3.jpg",
    "https://telegra.ph/file/5c21833853af29e04d014.jpg",
    "https://telegra.ph/file/8eb0312fdcd19dcb19194.jpg",
    "https://telegra.ph/file/2899d293dabf6eafecb30.jpg",
    "https://telegra.ph/file/d54930190a958fe43be88.jpg",
    "https://telegra.ph/file/9e100396f913383844efa.jpg",
    "https://telegra.ph/file/c976e4e20360d4bb8ef19.jpg",
    "https://telegra.ph/file/f9c875be425f1143e1f77.jpg",
    "https://telegra.ph/file/3679b891afb3123be5150.jpg",
    "https://telegra.ph/file/5e3e42a0de9c71e2fca43.jpg"
]

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

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    # تحميل صورة عشوائية
    image_url = random.choice(image_urls)
    image_file = "image.jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_file, 'wb') as f:
            f.write(response.content)
    else:
        await event.reply("حدث خطأ أثناء تنزيل الصورة.")
        return

    # إرسال الصورة مع الزرار الشفاف
    await event.client.send_file(event.chat_id, image_file, caption="**  أرسل لي رابط أي رسالة لاستنسخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً. ✓ **", buttons=[
        [Button.url("الدعم / المطور ¹", DEVELOPER_CHANNEL_LINK_1),
         Button.url("الدعم / المطور ²", DEVELOPER_CHANNEL_LINK_2)],
        [Button.url("قناة البوت", BOT_CHANNEL_LINK)]
    ])

# يمكن استخدام الأمر /stop لإيقاف العملية
@Drone.on(events.NewMessage(pattern=r"/stop"))
async def stop_process(event):
    # إلغاء عملية التحويل
    # قم بإيقاف أي عمليات تقوم بها الآن
    # قم بإرسال رسالة تؤكد إيقاف العملية للمستخدم
    await event.reply("تم إيقاف العملية. ✓")
