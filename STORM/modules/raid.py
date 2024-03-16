import asyncio

from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from STORMDB.data import STORMS, RAID, HRAID, LOVERAID, EMOJI, BDAY, SRAID, FLIRT, ABUSE
from config import OWNER_ID, SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], ["."]))
async def raid(xspam: Client, message: Message):  
      kex = message.text.split(" ")

      if len(kex) > 2:
            ok = await xspam.get_users(kex[2])  
            id = ok.id
            if id in STORMS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
            elif id == OWNER_ID:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
            elif id in SUDO_USERS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
            else:
                  counts = int(kex[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      elif message.reply_to_message and (len(kex) == 2):
            user_id = message.reply_to_message.from_user.id
            ok = await xspam.get_users(user_id)
            id = ok.id
            if id in STORMS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
            elif id == OWNER_ID:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
            elif id in SUDO_USERS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
            else:
                  counts = int(kex[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      else:
          await message.reply_text(".ʀᴀɪᴅ 10 <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


rusers = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], ["."]))
async def rraid(xspam: Client, message: Message):
      global rusers
      kex = message.text.split(" ")

      if len(kex) > 1:
          ok = await xspam.get_users(kex[1])
          id = ok.id
          if id in STORMS:
                await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
          elif id == OWNER_ID:
                await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
          elif id in SUDO_USERS:
                await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
          else:
              rusers.append(id)
              await message.reply_text("ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          if user_id in STORMS:
                await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
          elif user_id == OWNER_ID:
                await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
          elif user_id in SUDO_USERS:
                await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
          else:
              rusers.append(user_id)
              await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

      else:
          await message.reply_text(".ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["drraid", "draid", "dreplyraid"], ["."]))
async def draid(xspam: Client, message: Message):
      global rusers
      kex = message.text.split(" ")

      if len(kex) > 1:
          ok = await xspam.get_users(kex[1])
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

      else:
          await message.reply_text(".ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
    

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
      global rusers
      id = msg.from_user.id
      if id in rusers:
            reply = choice(RAID)
            await msg.reply_text(reply)


# HRAID
            
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["hraid"], ["."]))
async def hraid(xspam: Client, message: Message):  
      kex = message.text.split(" ")

      if len(kex) > 2:
            ok = await xspam.get_users(kex[2])
            id = ok.id
            if id in STORMS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
            elif id == OWNER_ID:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
            elif id in SUDO_USERS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
            else:
                  counts = int(kex[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(HRAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      elif message.reply_to_message and (len(kex) == 2):
            user_id = message.reply_to_message.from_user.id
            ok = await xspam.get_users(user_id)
            id = ok.id
            if id in STORMS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
            elif id == OWNER_ID:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
            elif id in SUDO_USERS:
                  await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
            else:
                  counts = int(kex[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(HRAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      else:
          await message.reply_text(".ʜʀᴀɪᴅ 10 <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["loveraid"], ["."]))
async def loveraid(xspam: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await xspam.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(LOVERAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(LOVERAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("!ʟᴏᴠᴇʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")          

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["emoji"], ["."]))
async def emoji(xspam: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await xspam.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(EMOJI)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(EMOJI)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("!ʟᴏᴠᴇʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["bspam"], ["."]))
async def bspam(xspam: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await xspam.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(BDAY)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(BDAY)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("!ʟᴏᴠᴇʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")    

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sraid"], ["."]))
async def sraid(xspam: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await xspam.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(SRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(SRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("!ꜱʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")                

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["flirt"], ["."]))
async def flirt(xspam: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await xspam.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(FLIRT)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(FLIRT)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("!ꜰʟɪʀᴛ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")               

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["abuse"], ["."]))
async def abuse(xspam: Client, e: Message):
      kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(kex) == 2:
          ok = await xspam.get_users(kex[1])
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(ABUSE)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          counts = int(kex[0])
          for _ in range(counts):
                reply = choice(ABUSE)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("!ᴀʙᴜꜱᴇ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")              

 
