import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

import pyshorteners

from aiogram import executor

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6262360381:AAF6IxcurQ1vvst1RX3ISMvu25HWuMDxK1E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
s = pyshorteners.Shortener()

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Отправляет приветственное сообщение
    """
    await message.answer("Привет! Я бот для сокращения ссылок. Просто отправь мне ссылку, и я сокращу её.")

# Обработка всех текстовых сообщений
@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_shorten_link(message: types.Message):
    """
    Обработка текстовых сообщений (ссылок) и сокращение ссылок.
    """
    if message.text.startswith('http'):
        shortened_url = s.tinyurl.short(message.text)  # Выберите нужный сервис сокращения
        await message.reply(f"Ваша сокращенная ссылка: {shortened_url}", parse_mode=ParseMode.MARKDOWN)
    else:
        await message.reply("Пожалуйста, отправьте мне корректную ссылку.")

if __name__ == '__main__':
    from aiogram import executor
    from aiogram import types

    # Установите мидлварь для логгирования
    from aiogram.contrib.middlewares.logging import LoggingMiddleware
    dp.middleware.setup(LoggingMiddleware())

    executor.start_polling(dp, skip_updates=True)
