# -*- coding: utf-8 -*- #

from telethon import TelegramClient, events
import re
import config

api_id = config.api_id
api_hash = config.api_hash
my_channel_id = config.my_channel_id
channels = config.channels
client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")


@client.on(events.Album(chats=channels))
async def handler(event):
    global text_message
    try:
        if event.original_update.message.message != '':
            text_message = str(event.original_update.message.message.split('\n', 1)[0])
            print(text_message)
            try:
                # Проверка на наличие ссылок в альбоме
                re.search("(?P<url>https?://[^\s]+)", event.original_update.message.message).group()
            except:

                await client.send_message(my_channel_id, file=event.messages, message=text_message)
        else:
            print('Ошибка')
    except:
        print('Ошибка')


client.start()
client.run_until_disconnected()
