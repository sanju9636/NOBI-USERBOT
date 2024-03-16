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

**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpextra`  
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpspam` 
**» ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpdm`
**» ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helplove`
**» ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpfun`
**» ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpnews`
**» ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpconvert`
**» ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpinfo`
**» ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpcreate`
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=FIRST_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=FIRST_TEXT)
