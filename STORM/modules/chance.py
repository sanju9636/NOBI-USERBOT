import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

# Define the chance command handler
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["chance"], [hl]))
async def chance(client, message):
    # Check if the command format is correct
    if hl + "chance " in message.text:
        # Extract the text following the /chance command
        text = message.text.split(hl + "chance ", maxsplit=1)[1]
        
        # Calculate a random chance percentage
        chance_percentage = random.randint(1, 100)
        
        # Edit the original message to include the calculated chance
        await message.edit(f"{text}\n\nChance: {chance_percentage}%")
    else:
        # Handle incorrect command format
        await message.reply("Invalid command format. Please use /chance <text>")
