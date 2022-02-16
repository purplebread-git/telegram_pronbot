# -*- coding: utf-8 -*- #
import re
from dispatcher import dp, bot
from config import admin_id
from bot import action

count = 0
check_media_group = [[], []]
check_media_group1 = [[], []]


@dp.message_handler(commands='send')
async def message_handler(message):
    await action()


@dp.message_handler(content_types=["photo", 'video'])
async def message_handler(message):
    msg = message
    media_group_id = message.media_group_id
    if len(check_media_group[0]) == 0:
        check_media_group[0].append(media_group_id)
        check_media_group1[0].append(msg)
    else:
        if len(check_media_group[0]) == 1 and len(check_media_group[1]) == 0:
            if check_media_group[0][0] == media_group_id:
                check_media_group[1].append(media_group_id)
                check_media_group1[1].append(msg)

        elif len(check_media_group1[0]) == 1 and len(check_media_group1[1]) == 1:
            await create_content(check_media_group1)
            check_media_group[0] = []
            check_media_group[1] = []
            check_media_group1[0] = []
            check_media_group1[1] = []
            check_media_group[0].append(media_group_id)
            check_media_group1[0].append(msg)
        else:
            print('Ошибка')
            check_media_group[0] = []
            check_media_group[1] = []
            check_media_group1[0] = []
            check_media_group1[1] = []


async def create_content(content):
    global con_title, type_con_1, file_id_con_1, type_con_2, file_id_con_2
    con_1 = content[0][0]
    con_2 = content[1][0]
    try:
        con_title = ' '.join((list(filter(None, re.split('\W|\d', con_1['caption'])))))
        check_true = True
    except:
        try:
            con_title = ' '.join((list(filter(None, re.split('\W|\d', con_2['caption'])))))
            check_true = True
        except:
            check_true = False
            await bot.send_message(admin_id, 'Нет описания для контента')
    if check_true:
        try:
            file_id_con_1 = con_1['photo'][0]['file_id']
            type_con_1 = 'photo'
        except:
            try:
                file_id_con_1 = con_1['video']['file_id']
                type_con_1 = 'video'
            except:
                await bot.send_message(admin_id, 'Ошибка c первым вложением')

        try:
            file_id_con_2 = con_2['photo'][0]['file_id']
            type_con_2 = 'photo'
        except:
            try:
                file_id_con_2 = con_2['video']['file_id']
                type_con_2 = 'video'
            except:
                await bot.send_message(admin_id, 'Ошибка cо вторым вложением')
        try:
            with open('porn/porn.txt', 'a') as f:
                text = str(
                    con_title + '\n' + type_con_1 + '\n' + file_id_con_1 + '\n' + type_con_2 + '\n' + file_id_con_2 + '\n\n')
                print(con_title)
                f.write(text)
        except:
            await bot.send_message(admin_id, 'Ошибка с записью')
