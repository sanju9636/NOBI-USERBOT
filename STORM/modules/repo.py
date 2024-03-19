from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["repo"], ["."]))
async def repo(client, message):
    msg = f"""
    ** ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ **

    • **ɢɪᴛʜᴜʙ** » [click here](https://github.com/sanju9636/NOBI-USERBOT) 
    • **ꜱᴜᴘᴘᴏʀᴛ** » [click here](https://t.me/HerokuCCBins) 
    • **ᴜᴘᴅᴀᴛᴇꜱ** » [click here](https://t.me/HerokuCCBins)
    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » [click here](https://t.me/TitanXSupport)
    
    **ʙʏ @OP_SHIVA_007**
    """
    await message.edit(msg)
