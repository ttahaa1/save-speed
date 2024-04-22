from pyrogram.errors import FloodWait, InviteHashInvalid, InviteHashExpired, UserAlreadyParticipant
from telethon import errors, events

import asyncio, subprocess, re, os, time
from pathlib import Path
from datetime import datetime as dt

# الانضمام إلى الدردشة الخاصة -----------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "**✨ تم الانضمام بنجاح إلى القناة ✨**"
    except UserAlreadyParticipant:
        return "**المستخدم مشترك بالفعل.**"
    except (InviteHashInvalid, InviteHashExpired):
        return "**لا يمكن الانضمام. ربما انتهت صلاحية الرابط أو غير صالح.**"
    except FloodWait:
        return "**طلبات كثيرة جدًا، جرب مرة أخرى في وقت لاحق.**"
    except Exception as e:
        print(e)
        return "**لا يمكن الانضمام، جرب الانضمام يدويًا.**"
    
# Regex ---------------------------------------------------------------------------------------------------------------

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return "**🔗 الرابط المحدد:** " + link
        else:
            return False
    except Exception:
        return False
    
# Screenshot ---------------------------------------------------------------------------------------------------------------

def hhmmss(seconds):
    x = time.strftime('%H:%M:%S',time.gmtime(seconds))
    return "**⏱️ الزمن المحدد:** " + x

async def screenshot(video, duration, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    time_stamp = hhmmss(int(duration)/2)
    out = dt.now().isoformat("_", "seconds") + ".jpg"
    cmd = ["ffmpeg",
           "-ss",
           f"{time_stamp}", 
           "-i",
           f"{video}",
           "-frames:v",
           "1", 
           f"{out}",
           "-y"
          ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    if os.path.isfile(out):
        return "**📸 لقطة الشاشة:** " + out
    else:
        return None
