from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dice"], ["."]))
async def dice(client: Client, message: Message):
    await message.edit("🎲")
