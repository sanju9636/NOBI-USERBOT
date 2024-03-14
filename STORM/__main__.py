import asyncio
import importlib
from pyrogram import Client, idle
from STORM.helper import join
from STORM.modules import ALL_MODULES
from STORM import clients, ids

async def start_bot():
    #await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("STORM.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            await join(cli)
            print(f"Started {cli.me.first_name} 🔥")
            ids.append(cli.me.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    print("clients stopped.")
    for cli in clients:
        try:
            await cli.stop()
        except Exception as e:
            print(f"{e}")

if __name__ == "__main__":
    asyncio.run(start_bot())
