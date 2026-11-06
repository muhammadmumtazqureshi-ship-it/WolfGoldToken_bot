import telebot, os
from telebot import types

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID =  7382910455
WEBAPP_URL = "https://muhammadmr.github.io/WolfGoldToken_bot/"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⛏️ Open WGT Mining App", web_app=types.WebAppInfo(url=WEBAPP_URL)))
    markup.add(types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/WolfGoldToken"))
    text = "🐺💎 *WOLF GOLD TREASURY (WGT)* 💎🐺\n\n🔥 The Golden Wolf of Solana!\n\n🪙 WGT - Luxury Gold Token\n⛓️ Solana Blockchain\n\n👇 Mining App Open Karo aur Gold Mine Karo!\n\n💰 /mine - Mining App\n💎 /balance - Balance\n👑 /admin - Admin Panel"
    try:
        with open('wgt.png','rb') as p:
            bot.send_photo(m.chat.id, p, caption=text, parse_mode='Markdown', reply_markup=markup)
    except:
        bot.send_message(m.chat.id, text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['mine','app'])
def mine(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⛏️ Open Mining Dashboard", web_app=types.WebAppInfo(url=WEBAPP_URL)))
    bot.send_message(m.chat.id, "⛏️ WGT Mining Dashboard Open Karo!", reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin(m):
    if m.from_user.id==ADMIN_ID:
        bot.send_message(m.chat.id, "👑 Admin Ustad! Panel ready!")
    else:
        bot.send_message(m.chat.id, "❌ Only Admin!")

@bot.message_handler(func=lambda x: True)
def allmsg(m):
    bot.send_message(m.chat.id, "🐺 /start dabao Ustad!")

print("WGT Bot Started")
bot.infinity_polling()
