import telebot

bot = telebot.TeleBot("5534979217:AAH7rex-IQH6z53BAPNGhyvaMPIL6PyKEPY")

@bot.message_handler(commands=['start'])
def start(message):
    mes = f'Привет , <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id ,mes, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if(message.text == "Hello"):
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')

bot.polling(none_stop=True)