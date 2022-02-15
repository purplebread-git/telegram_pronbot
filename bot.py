import aioschedule
import asyncio
import random
import handlers
from aiogram import executor, types
from dispatcher import dp
from dispatcher import bot
from config import admin_id, kanals
from read_links import links

ver = 1.0


def random_choice():
    numbers_of_kanals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    first_group = (random.sample(numbers_of_kanals, 3))
    for i in first_group:
        numbers_of_kanals.remove(i)
    second_group = (random.sample(numbers_of_kanals, 3))
    for i in second_group:
        numbers_of_kanals.remove(i)
    thirst_group = numbers_of_kanals
    return first_group, second_group, thirst_group


async def send_media_group(content, group):
    media = types.MediaGroup()

    title = content[0]
    type_con_1 = content[1]
    file_id_con_1 = content[2]
    type_con_2 = content[3]
    file_id_con_2 = content[4]

    if type_con_1 == 'photo':
        media.attach_photo(types.InputMediaPhoto(file_id_con_1, caption=title))
    elif type_con_1 == 'video':
        media.attach_video(types.InputMediaVideo(file_id_con_1, caption=title))
    else:
        print('Ошибка')

    if type_con_2 == 'photo':
        media.attach_photo(types.InputMediaPhoto(file_id_con_2))
    elif type_con_2 == 'video':
        media.attach_video(types.InputMediaVideo(file_id_con_2))
    else:
        print('Ошибка')

    for i in range(0, len(group)):
        await bot.send_media_group(kanals[group[i]], media)


async def action():
    groups = random_choice()
    try:
        content = links()
        await send_media_group(content, groups[0])
    except:
        await bot.send_message(admin_id, 'Ошибка с отправкой контента в первой группе')
    try:
        content = links()
        await send_media_group(content, groups[1])
    except:
        await bot.send_message(admin_id, 'Ошибка с отправкой контента во второй группе')
    try:
        content = links()
        await send_media_group(content, groups[2])
    except:
        await bot.send_message(admin_id, 'Ошибка с отправкой контента в третьей группе')


async def scheduler():
    aioschedule.every().day.at("09:00").do(action)
    aioschedule.every().day.at("12:00").do(action)
    aioschedule.every().day.at("15:00").do(action)
    aioschedule.every().day.at("18:00").do(action)
    aioschedule.every().day.at("21:00").do(action)
    aioschedule.every().day.at("23:59").do(action)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
print('Version bot - ', ver)
