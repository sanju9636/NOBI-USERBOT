from pyrogram import Client, filters
from pyrogram.types import Message
from googlesearch import search
from config import SUDO_USERS
# Function to perform a Google search and return top search results

def google_search(query, num_results=5):
    results = []
    for result in search(query, num_results=num_results, stop=num_results, pause=2):
        results.append(result)
    return results

# Define the football command handler
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["google"], ["."]))
async def google(client, message):
    # Extract the search query from the message
    query = message.text.split(".google", maxsplit=1)[1]
    
    # Perform Google search
    search_results = google_search(query)
    
    # Prepare and send the response message
    response = "**ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʀᴇꜱᴜʟᴛꜱ**:\n"
    for idx, result in enumerate(search_results, start=1):
        response += f"{idx}. {result}\n"
    await message.reply(response)
