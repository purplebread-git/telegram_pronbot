# telegram_pronbot

#### Этот бот создан для граббинга медиафайлов с каналов telegram 18+ и рассылки по вашим каналам
`python: 3.7` `aiogram: 2.16` `telethon: 1.24.0` `aioschedule: 0.5.2` `python-decouple: 3.6` 




------------

Я решил разделить задачу на двух ботов:

      bot.py           (aiogram)       Используется для приема, записи и отправки контента по нужным нам каналам
      grabber.py       (telethon)      Используется для отслеживания и отправки нового контента среди чужих каналов
      
grabber.py
------------
Работает довольно просто. Весь контент, отправленный альбомом в каналах указанных в `config.py.CHANNELS_FOR_GRAB` фильтрует и отправляет нашему боту `bot.py` для дальнейшей обработки.

bot.py
------------
Получает на вход контент от `grabber.py`. Обрабатывает с помощью `handlers/personal_actions.py` и записывает в `porn/porn.txt`

Запуск
------------
Найдите `config.py` и подставьте свои данные в переменные. В исходной версии используется библиотека `decouple` для подкачивания данных в переменные из файла `.env`.  
  
Рекомендую добавить файл `.env` в корень telegram_pronbot и прописать там следующее:
```
BOT_TOKEN = Токен бота
ADMIN_ID = ID твоего аккаунта, через который будет работать client grabber.py
CHANNELS_FOR_SEND = ID каналов для отправки сформированного контента
API_ID = Айди API приложения Telegram
API_HASH = Хэш API приложения Telegram 
BOT_ID = ID твоего бота
CHANNELS_FOR_GRAB = ID каналов, которые нужно будет "грабить"
```
- BOT_TOKEN - @BotFather в telegram  
- API_ID и API_HASH - https://my.telegram.org/auth?to=apps  
- Для определения ID каналов, себя и бота можете воспользоваться @getmyid_bot в telegram  
  
Запускаем `bot.py` и `grabber.py` и наслаждаемся результатом!

