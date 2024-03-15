from pyrogram import Client, filters

@Client.on_message(filters.user(OWNER_ID) & filters.command(["id"], ["."]))
async def find_id(client, message):
    if message.reply_to_message is None:
        await message.edit(f"ᴄʜᴀᴛ ɪᴅ » `{message.chat.id}`")
    else:
        await message.edit(f"ᴜsᴇʀ ɪᴅ » `{message.reply_to_message.from_user.id}`\nᴄʜᴀᴛ ɪᴅ » `{message.chat.id}`")
