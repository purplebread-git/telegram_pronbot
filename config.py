from decouple import config

# for bot.py

BOT_TOKEN = config('BOT_TOKEN', default='')  # Токен бота

admin_id = config('admin_id', default='')  # Твой айди аккаунта

kanals = config('kanals', default='')  # Список айди каналов, по которым бот будет рассылать контент

# for grabber.py

api_id = config('api_id', default='')  # Id аккаунта
api_hash = config('api_hash', default='')  # Hash аккаунта

my_channel_id = config('my_channel_id', default='')  # Айди бота, в который grabber будет пересылать контент
channels = config('channels', default='')  # Список каналов с которых grabber будет парсить контент
