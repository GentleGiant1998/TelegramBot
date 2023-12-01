import datetime
import locale

import telebot

bot = telebot.TeleBot('6575657548:AAGKU2_1iFvEzqLsM43wlfjxBZv6_SQMN2o')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Дарова!")


@bot.message_handler(func=lambda message: True)
def all_message(message):
    if message.text == 'Какой сегодня день?':
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        date = datetime.datetime.today()
        formatted_date = date.strftime("%d-%m-%Y, %a")
        bot.reply_to(message, formatted_date)

bot.polling()
