import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔐 Токен твоего бота
API_TOKEN = '7851005057:AAHVVT0i4OQbw-Dq9ZHAp5OOId3RK3xFKhg'

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Простой хендлер команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать! ⭐️ Здесь вы можете купить звёзды.")

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
