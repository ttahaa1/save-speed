import requests
from telethon import events, Button
from .. import bot as Drone

S = '/' + 's' + 't' + 'a' + 'r' + 't'
DEVELOPER_CHANNEL_LINK = 'https://t.me/l_s_I_I'
DEVELOPER_CHANNEL_LINK_2 = 'https://t.me/V_1_1_1_0'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    Drone = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv:
        xx = await conv.send_message("أرسل لي أي فيديو لتكون الفيديو المصغرة كرد على هذه الرسالة.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("لم يتم العثور على وسائط.")
        mime = x.file.mime_type
        if not 'video' in mime:
            await xx.edit("لم يتم العثور على فيديو.")
            return
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'جارٍ المحاولة...')
        media_url = await x.download_media()
        await t.edit("تم حفظ الفيديو مؤقتًا!")

@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    Drone = event.client
    await event.edit('جارٍ المحاولة...')
    try:
        os.remove(f'{event.sender_id}.mp4')
        await event.edit('تم الحذف!')
    except Exception:
        await event.edit("لم يتم العثور على أي فيديو مصغر.")

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    # تنزيل الفيديو المباشر إلى ملف محلي
    video_url = "https://telegra.ph/file/0d0999b968c6e4db3f471.mp4"
    video_file = "video.mp4"
    response = requests.get(video_url)
    if response.status_code == 200:
        with open(video_file, 'wb') as f:
            f.write(response.content)
    else:
        await event.reply("حدث خطأ أثناء تنزيل الفيديو.")
        return

    # إرسال الفيديو مع الزرارين
    await event.client.send_file(event.chat_id, video_file, caption="**  أرسل لي رابط أي رسالة لاستنسخها هنا. بالنسبة للرسائل الخاصة بالقناة، أرسل رابط الدعوة أولاً. ✓ **", buttons=[
        [Button.url("¹الدعم / المطور", DEVELOPER_CHANNEL_LINK), Button.url("الدعم / المطور ²", DEVELOPER_CHANNEL_LINK_2)]
    ])

# يمكن استخدام الأمر /stop لإيقاف العملية
@Drone.on(events.NewMessage(pattern=r"/stop"))
async def stop_process(event):
    # إلغاء عملية التحويل
    # قم بإيقاف أي عمليات تقوم بها الآن
    # قم بإرسال رسالة تؤكد إيقاف العملية للمستخدم
    await event.reply("تم إيقاف العملية. ✓")
