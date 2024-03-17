from pyrogram import Client, filters
from pyrogram.types import Message
from googlesearch import search

# Function to perform a Google search and return top search results
def google_search(query, num_results=5):
    results = []
    for result in search(query, num=num_results, stop=num_results, pause=2):
        results.append(result)
    return results

# Define the football command handler
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["google"], ["."]))
async def google(client, message: Message):
    # Extract the search query
    query = message.text.split(".", maxsplit=1)[1].strip()

    # Perform Google search
    search_results = google_search(query)

    # Prepare the response message
    response = "**ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʀᴇꜱᴜʟᴛꜱ**:\n"
    for idx, result in enumerate(search_results, start=1):
        response += f"{idx}. {result}\n"

    # Send the response
    await message.reply(response)
