from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

DM_TEXT = f"""
**ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}dmspam` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴅᴏ ᴅᴍ ꜱᴘᴀᴍ ᴏɴ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ....

• `{hl}dmraid` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴅᴏ ᴅᴍ ʀᴀɪᴅ ᴏɴ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpdm"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=DM_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=DM_TEXT)
