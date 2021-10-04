import os
from dotenv import load_dotenv

from telethon import TelegramClient as opc
from telethon.sessions import StringSession as shashankxD
from telethon import events
from telethon import functions

load_dotenv()
sudo = []

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")
SUDO_USER = os.environ.get("SUDO_USERS")

if STRING_SESSION:
  shashank = opc(shashankxD(STRING_SESSION), api_id=api_id, api_hash=api_hash).start()
  print('SUCCESSFULLY STARTED CLIENT')
else:
  print('COULD NOT FOUND STRING SESSION PLESSE CHECK VARS')
  
@shashank.on(events.NewMessage(incoming=True, pattern='*gcast'))
async def gcast(event):
  if event.sender_id == SUDO_USERS:
    if event.is_reply:
      msg_t = str(event.raw_text[7:])
      await event.edit('processing')
      reply_msg = event.get_reply_message()
      chat_n = 0
      failed_chat = 0
      try:
        async for chat in shashank.iter_dialogs():
          id = chat.id
          chats.append(id)
        if msg_t.lower() == "loud":
          try:
            for x in chats:
              try:
                kk = await shashank.message(x, reply_mgs)
                try:
                  await shashank.pin_message(x, kk.id)
                except Exception as e:
                  failed_chat += 1
            await event.reply(f"""
            *__Gcast completed__*
            
            __Completed gcast {chat_n}__
            __Failed in chat {failed_chat}__""")
            
shashank.run_until_disconnected()
