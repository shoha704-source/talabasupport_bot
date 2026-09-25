import telebot

TOKEN = "8028825414:AAHTWPs4dWZTSMImZq6n7yCdS_rBeq0Q324"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 🤖\n\n"
        "Men sizning AI yordamchingizman.\n"
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