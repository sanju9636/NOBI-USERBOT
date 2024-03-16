from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
import time
from pyrogram import Client, filters
from config import HELP_PIC, SUDO_USERS
from pyrogram.types import InlineQueryResultPhoto as IQRP

hl = "."

PIC = HELP_PIC

HELP_TEXT = "**• ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ**\n\n**• ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ʟᴏᴀᴅᴇᴅ ᴡɪᴛʜ 150+ ᴄᴏᴍᴍᴀɴᴅꜱ 🍷**\n\n• **ʙʏ @kexx_xd** 🥂\n\n**• ᴘᴀɢᴇ** - `1/2`"
HELP_TEXTT = "****• ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ**\n\n**• ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ʟᴏᴀᴅᴇᴅ ᴡɪᴛʜ 150+ ᴄᴏᴍᴍᴀɴᴅꜱ 🍷**\n\n• **ʙʏ @kexx_xd** 🥂\n\n**• ᴘᴀɢᴇ** - `2/2`**"

EXTRA_MSG = f"""
**ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ** 

• `{hl}ping` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ....

• `{hl}restart` » ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ....

• `{hl}alive` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ...

• `{hl}repo` » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ...

• `{hl}id` » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ'ꜱ ᴜꜱᴇʀ_ɪᴅ....

• `{hl}gitinfo` <username> » ᴛᴏ ɢᴇᴛ ɢɪᴛ ᴀᴄᴄ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....
"""

SPAM_MSG = f"""
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

LOVE_MSG = f"""
**ʟᴏᴠᴇ ꜱʜᴏᴡᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}lover` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}flirt` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}hflirt` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}loveraid` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}sraid` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....
"""

FUN_MSG = f"""
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

NEWS_MSG = f"""
**ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}news` » ᴛᴏ ɢᴇᴛ ᴛᴏᴘ 5 ʜᴇᴀᴅʟɪɴᴇꜱ ᴏꜰ ɴᴇᴡꜱ....

• `{hl}weather (ʏᴏᴜʀ ᴄɪᴛʏ)` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....
"""

CONVERT_MSG = f"""
**ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}tts` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ....
"""

INFO_MSG = f"""
**ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}info` » ᴛᴏ ɢᴇᴛ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ ᴀᴄᴄ....
"""

CREATE_MSG = f"""
**Create Commands**

• `{hl}create group (name)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ɢʀᴏᴜᴘ....

• `{hl}create channel (name)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ....
"""

DEV_MSG = f"""
**ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ ɪɴꜰᴏ**

• ☰ RiZoeL - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/ItsRiZoeL)

• ⏤͟͞〲ʟᴜ͢ᴄᴋʏ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Kexx_XD)

• R I K - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/aka_rik_ded)
"""

SUPPORT_MSG = f"""
**ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛ**

• ⏤͟͞〲ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/STORM_CHATZ)

• ⏤͟͞〲ᴛᴇᴄʜ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/STORM_TECHH)

• ⏤͟͞〲ꜱᴛᴏʀᴍ ʜᴇʟᴘ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/rasedidstore)
"""

FUNGRP_MSG = f"""
**ꜰᴜɴ ɢʀᴏᴜᴘ**

• ⏤͟͞〲ꜰʀɪᴇɴᴅ ᴄᴀꜱᴛᴇʟ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/FriendCastel)
"""

NOTE_MSG = f"""
**ᴀ ɴᴏᴛᴇ**

                      ❗️YOU ARE FOREWARNED❗️

                       ⚠️ ᴡᴀʀɴɪɴɢ ꜰᴏʀ ʏᴏᴜ ⚠️

! We won't be responsible for any kind of ban due to this bot.
! Bot Spam was made for fun purpose and to make group management easier.
! It's your concern if you spam and gets your account banned.
! Also, Forks won't be entertained.
! If you fork this repo and edit plugins, it's your concern for further updates.
! using Repo is fine. But if you edit something we will not provide any help.
! In short, use At Your Own Risk    

               💖 Thanks for using our bot 💖

• ʀᴇᴘᴏ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/VARC9210/STORM-USERBOT)              
"""

HELP_BUTTON = IKM(
              [
              [
              IKB("• ᴄʀᴇᴀᴛᴇ •", callback_data='create'),
              IKB("• ɴᴇᴡꜱ •", callback_data='news')
              ],
              [
              IKB("• ᴇxᴛʀᴀ •", callback_data="extra"),
              IKB("• ʟᴏᴠᴇ •", callback_data="love")
              ],
              [
              IKB("• ꜱᴘᴀᴍ •", callback_data="spam"),
              IKB("• ꜰᴜɴ •", callback_data='fun')
              ],
              [
              IKB("• ɪɴꜰᴏ •", callback_data='info'),
              IKB("• ᴄᴏɴᴠᴇʀᴛ •", callback_data='convert')
              ],
              [
              IKB(" ʜᴏᴍᴇ 🏠", callback_data='home')
              ]
              ]
              )

                
HELP_MARKUP = IKM(
              [
              [
              IKB("• ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ •", callback_data="dev")
              ],
              [
              IKB("• ꜱᴜᴘᴘᴏʀᴛ •", callback_data="support")
              ],
              [
              IKB("• ꜰᴜɴɢʀᴘ •", callback_data="fungrp  ")
              ],
              [
              IKB("• ɴᴏᴛᴇ •", callback_data="note")
              ],
              [
              IKB("2ɴᴅ ᴘᴀɢᴇ 📃", callback_data="2page")
              ]
              ]
              )
sux = None

BACK = IKM(
       [
       [
       IKB("🔙", callback_data="back")
       ]
       ]
       )

X = IKM(
    [
    [
    IKB("➡️", callback_data="x")
    ]
    ]
    )

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], ["."]))
async def help(client, message):
    global sux
    if not sux:
        sux = Client.me.username
    await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    try:
        nice = await client.get_inline_bot_results(bot=sux, query="inline_help")
    except Exception as e:
        return await message.reply(e)
    try:
        await message.delete()
        await message.delete()
    except:
        pass
    try:
        await client.send_inline_bot_result(message.chat.id, nice.query_id, nice.results[0].id)
    except Exception as e:
        await message.reply(e)

ans = [IQRP(photo_url=HELP_PIC, thumb_url=PIC, title="Help", description="Help Menu", caption=HELP_TEXT, reply_markup=HELP_MARKUP)]

@Client.on_inline_query()
async def inl(y, x):
    text = x.query.lower()
    try:
        if text == "inline_help":
            await y.answer_inline_query(x.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)

@Client.on_callback_query(filters.regex("ʙᴀᴄᴋ"))
async def back(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)

@Client.on_callback_query(filters.regex("extra"))
async def extra(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=EXTRA_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("spam"))
async def spam(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SPAM_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("love"))
async def love(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=LOVE_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("dev"))
async def profile(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=DEV_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("fun"))
async def profile(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUN_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("note"))
async def profile(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=NOTE_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("2page"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXTT, reply_markup=HELP_BUTTON)

@Client.on_callback_query(filters.regex("x"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXTT, reply_markup=HELP_BUTTON)

@Client.on_callback_query(filters.regex("fun"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUN_MSG, reply_markup=BACK)

@Client.on_callback_query(filters.regex("support"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SUPPORT_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("news"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=NEWS_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("convert"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=CONVERT_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("home"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)

@Client.on_callback_query(filters.regex("info"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=INFO_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("fungrp"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUNGRP_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("news"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=NEWS_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("note"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=NOTE_MSG, reply_markup=X)

@Client.on_callback_query(filters.regex("create"))
async def pange(client, message):
    if message.from_user.id != Client.me.id:
        return await message.answer("Tᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ......", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=CREATE_MSG, reply_markup=X)
