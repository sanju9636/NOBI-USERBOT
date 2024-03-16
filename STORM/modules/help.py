import heroku3

from os import getenv
from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

FIRST_TEXT = f"""
✨ **ʙᴏᴛ ʜᴇʟᴘ** ✨

**[ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ](https://t.me/Kexx_XD) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ꜱᴛᴏʀᴍ](https://github.com/VARC9210/STORM-USERBOT)** ✨

**ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳](https://t.me/STORM_TECHH)**
**ꜱᴜᴘᴘᴏʀᴛ: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🇮🇳](https://t.me/STORM_CHATZ)**

**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help extra`  
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help spam` 
**» ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help dm`
**» ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help love`
**» ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help fun`
**» ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help news`
**» ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help convert`
**» ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help info`
**» ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl} help create`
"""

EXTRA_TEXT = f"""
**ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ** 

• `{hl}ping` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ....

• `{hl}restart` » ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ....
    
• `{hl}alive` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ...

• `{hl}repo` » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ...

• `{hl}id` » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ'ꜱ ᴜꜱᴇʀ_ɪᴅ....

• `{hl}gitinfo` <username> » ᴛᴏ ɢᴇᴛ ɢɪᴛ ᴀᴄᴄ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....
"""

SPAM_TEXT = f"""
**ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}spam` » ᴛᴏ ꜱᴘᴀᴍ ᴍᴇꜱꜱᴀɢᴇꜱ ʙʏ ᴄᴏᴜɴᴛ....

• `{hl}banall` » ᴛᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ᴏꜰ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛꜱ....

• `{hl}raid` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ....

• `{hl}replyraid` » ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ ᴏɴ ᴀɴʏᴏɴᴇ....

• `{hl}dreplyraid` » ᴛᴏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ....

• `{hl}abuse` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ....

• `{hl}bspam` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}hang` <ᴄᴏᴜɴᴛ> » ꜱᴘᴀᴍꜱ ʜᴀɴɢ ᴍꜱɢꜱ ɪɴ ᴄʜᴀᴛ.....
"""

DM_TEXT = f"""
**ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}dmspam` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴅᴏ ᴅᴍ ꜱᴘᴀᴍ ᴏɴ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ....

• `{hl}dmraid` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴅᴏ ᴅᴍ ʀᴀɪᴅ ᴏɴ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ....
"""

LOVE_TEXT = f"""
**ʟᴏᴠᴇ ꜱʜᴏᴡᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}lover` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}flirt` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}hflirt` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}loveraid` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}sraid` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....
"""

FUN_TEXT = f"""
**ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}lover` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}stupid` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}sex` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}chance` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}kiss` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}dare` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}truth` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}emoji` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....
"""

NEWS_TEXT = f"""
**ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}news` » ᴛᴏ ɢᴇᴛ ᴛᴏᴘ 5 ʜᴇᴀᴅʟɪɴᴇꜱ ᴏꜰ ɴᴇᴡꜱ....

• `{hl}weather (ʏᴏᴜʀ ᴄɪᴛʏ)` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....
"""

CONVERT_TEXT = f"""
**ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}tts` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ....
"""

INFO_TEXT = f"""
**ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}info` » ᴛᴏ ɢᴇᴛ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ ᴀᴄᴄ....
"""

CREATE_TEXT = f"""
**Create Commands**

• `{hl}create group (name)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ɢʀᴏᴜᴘ....

• `{hl}create channel (name)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=FIRST_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=FIRST_TEXT)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help extra"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=EXTRA_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=EXTRA_TEXT)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help spam"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=SPAM_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=SPAM_TEXT)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help dm"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=DM_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=DM_TEXT)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help love"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=LOVE_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=LOVE_TEXT)              

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help fun"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=FUN_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=FUN_TEXT)           

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help news"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=NEWS_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=NEWS_TEXT)             

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help convert"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=CONVERT_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=CONVERT_TEXT)                          

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help info"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=INFO_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=INFO_TEXT)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help create"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=CREATE_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=CREATE_TEXT)                                
