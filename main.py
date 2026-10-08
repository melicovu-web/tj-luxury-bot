import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("TOKEN") or os.getenv("BOT_TOKEN") or ""
TOKEN = TOKEN.strip()
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Салом! TJ Luxury Bot кор мекунад! ✅")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Паёматро гирифтам: {message.text}")

def run_bot():
    bot.infinity_polling()

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_flask()
