import telebot
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем токен
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен загружен
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден в .env файле")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

print("Эхо-бот запущен")
bot.polling() 