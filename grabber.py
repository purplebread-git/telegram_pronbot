import re
import config
from traceback import print_exc
from telethon import TelegramClient, events


API_ID = config.API_ID
API_HASH = config.API_HASH
BOT_ID = config.BOT_ID
CHANNELS_FOR_GRAB = config.CHANNELS_FOR_GRAB

client = TelegramClient('myGrab', API_ID, API_HASH)
print("GRAB - Started")


@client.on(events.Album(chats=CHANNELS_FOR_GRAB))
async def handler(event):
    await client.get_dialogs()
    global text_message
    try:
        if event.original_update.message.message != '':
            text_message = str(event.original_update.message.message.split('\n', 1)[0])
            print(text_message)
            try:
                # Проверка на наличие ссылок в альбоме
                re.search("(?P<url>https?://[^\s]+)", event.original_update.message.message).group()
            except:
                await client.send_message(BOT_ID, file=event.messages, message=text_message)
    except Exception:
        print_exc()

client.start()
client.run_until_disconnected()
