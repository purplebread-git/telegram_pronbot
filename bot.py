import aioschedule
import asyncio
import random
import handlers
import traceback
from aiogram import executor, types
from dispatcher import dp
from dispatcher import bot
from config import ADMIN_ID, CHANNELS_FOR_SEND
from read_links import links

ver = 1.0


# Функция разбивания каналов на 3 группы, чтобы не отправлять один и тот же контент сразу во все каналы
def random_choice():
    numbers_of_kanals = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                         9]  # 10 элементов, потому что у меня было 10 каналов в CHANNELS_FOR_SEND
    first_group = (random.sample(numbers_of_kanals, 3))
    for i in first_group:
        numbers_of_kanals.remove(i)
    second_group = (random.sample(numbers_of_kanals, 3))
    for i in second_group:
        numbers_of_kanals.remove(i)
    thirst_group = numbers_of_kanals
    return first_group, second_group, thirst_group


# Функция составления и отправки сообщения
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
        await bot.send_media_group(CHANNELS_FOR_SEND[group[i]], media)


# Функция main для запуска двух выше функций
async def action():
    groups = random_choice()
    try:
        content = links()
        await send_media_group(content, groups[0])
    except Exception:
        await bot.send_message(ADMIN_ID, 'Ошибка с отправкой контента в первой группе')
        traceback.print_exc()
    try:
        content = links()
        await send_media_group(content, groups[1])
    except Exception:
        await bot.send_message(ADMIN_ID, 'Ошибка с отправкой контента во второй группе')
        traceback.print_exc()
    try:
        content = links()
        await send_media_group(content, groups[2])
    except Exception:
        await bot.send_message(ADMIN_ID, 'Ошибка с отправкой контента в третьей группе')
        traceback.print_exc()


# Расписание отправки сообщений в каналы
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
    print('Version bot - ', ver)
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

