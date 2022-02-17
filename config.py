from decouple import config, Csv

# for bot.py

BOT_TOKEN = config('BOT_TOKEN')  # Токен бота.
ADMIN_ID = config('ADMIN_ID', cast=int)  # Твой айди аккаунта
CHANNELS_FOR_SEND = config('CHANNELS_FOR_SEND', cast=Csv(int))  # Список айди каналов, по которым бот будет рассылать контент

# for grabber.py

API_ID = config('API_ID', cast=int)  # Id аккаунта
API_HASH = config('API_HASH')  # Hash аккаунта
BOT_ID = config('BOT_ID', cast=int)  # Айди бота, в который grabber будет пересылать контент
CHANNELS_FOR_GRAB = config('CHANNELS_FOR_GRAB', cast=Csv(int))  # Список каналов с которых grabber будет парсить контент
