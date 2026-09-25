import telebot

TOKEN = "8028825414:AAH2NQjCi9H7nJZcVyP6oEL6v76LMkRtbLU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 🤖\n\n"
        "Men Talaba Support botman.\n"
        "Savolingizni yozing."
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.reply_to(
        message,
        "Xabaringizni oldim: " + message.text
    )

print("🤖 Bot ishga tushdi...")
bot.infinity_polling()