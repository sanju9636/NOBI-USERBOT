import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

# Define the chance command handler
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["chance"], [hl]))
async def chance(client, message):
    # Extract the text following the /chance command
    text = message.text.split(hl + "chance ", maxsplit=1)[1]
    
    # Calculate a random chance percentage
    chance_percentage = random.randint(1, 100)
    
    # Edit the original message to include the calculated chance
    await message.edit(f"{text}\n\nChance: {chance_percentage}%")

# Create a Pyrogram client instance
app = Client("my_bot")

# Run the client
app.run()
