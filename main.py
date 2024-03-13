from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle


CLIENTS = []

for SESSION in SESSIONS:
    if SESSION:
        client = Client(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="STORM"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("STORM_CHATZ")
            CLIENT.join_chat("STORM_TECHH")
            print(f"ꜱᴛᴏʀᴍ ᴀꜱt {i+1} ʜᴀꜱ ʙᴇᴇɴ ꜱᴛᴀʀᴛᴇᴅ....")
        except Exception as e:
            print(e)

    print("ʏᴏᴜʀ ᴘʏ-ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🥳🎉")
    idle()
