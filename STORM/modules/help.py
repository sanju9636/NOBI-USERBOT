import heroku3

from os import getenv
from config import SUDO_USERS, ALIVE_PIC

from pyrogram import Client, filters
from pyrogram.types import Message


FIRST_TEXT = f"""✨ **ʙᴏᴛ ʜᴇʟᴘ** ✨

**[ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ](https://t.me/Kexx_XD) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ꜱᴛᴏʀᴍ](https://github.com/VARC9210/STORM-USERBOT)** ✨

**ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳](https://t.me/STORM_TECHH)**
**ꜱᴜᴘᴘᴏʀᴛ: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🇮🇳](https://t.me/STORM_CHATZ)**

**» ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/rasedidstore/1072)
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/rasedidstore/1070)
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/rasedidstore/1069)
**» ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/rasedidstore/1071)"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], [".", "!", "/"]))
async def help(client: Client, message: Message):
    await client.send_photo(
        chat_id=message.chat.id,
        photo=ALIVE_PIC,
        caption=FIRST_TEXT
    )