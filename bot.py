import telebot, os
from telebot import types

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBAPP_URL = "https://muhammadmumtazqureshi-ship-it.github.io/WolfGoldToken_bot/"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⛏️ Open WGT Mining App", web_app=types.WebAppInfo(url=WEBAPP_URL)))
    markup.add(types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/WolfGoldToken"))
    text = "🐺💎 WOLF GOLD TREASURY (WGT) 💎🐺\n\nThe Golden Wolf of Solana Blockchain!\n\n⛏️ Mining Dashboard Live!\n💰 Earn WGT Tokens!\n\nClick below to start mining!"
    try:
        with open('token.jpg','rb') as p:
            bot.send_photo(m.chat.id, p, caption=text, parse_mode='Markdown', reply_markup=markup)
    except:
        bot.send_message(m.chat.id, text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['mine'])
def mine(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⛏️ Open Mining Dashboard", web_app=types.WebAppInfo(url=WEBAPP_URL)))
    bot.send_message(m.chat.id, "⛏️ WGT Mining Dashboard - Click to start!", reply_markup=markup)

@bot.message_handler(func=lambda x: True)
def allmsg(m):
    bot.send_message(m.chat.id, "🐺 Send /start to open WGT Mining App!")

print("Bot Started")
bot.infinity_polling()
