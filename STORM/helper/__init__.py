import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "STORM"])

async def join(client):
    try:
        await client.join_chat("STORM_CHATZ")
    except BaseException:
        pass
