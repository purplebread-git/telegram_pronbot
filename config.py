from decouple import config, Csv

# for bot.py

BOT_TOKEN = config('BOT_TOKEN')  # Токен бота

admin_id = config('admin_id', cast=int)  # Твой айди аккаунта

kanals = config('kanals', cast=Csv(int))  # Список айди каналов, по которым бот будет рассылать контент

# for grabber.py

api_id = config('api_id', cast=int)  # Id аккаунта
api_hash = config('api_hash')  # Hash аккаунта

my_channel_id = config('my_channel_id', cast=int)  # Айди бота, в который grabber будет пересылать контент
channels = config('channels', cast=Csv(int))  # Список каналов с которых grabber будет парсить контент
