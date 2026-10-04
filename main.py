import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Салом! TJ Luxury Bot 👑\n\nБот кор мекунад! Чӣ харидан мехоҳӣ?")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Паёмат: {message.text}")

@app.route('/')
def home():
    return "TJ Luxury Bot is Live!"

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
