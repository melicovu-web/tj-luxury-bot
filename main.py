import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Салом! TJ Luxury Bot кор мекунад! 🚀")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Ту навиштӣ: {message.text}")

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
