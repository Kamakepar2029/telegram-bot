# -*- coding: utf-8 -*-
import telebot
import config
import subprocess
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['ls'])
def welcome(message):
  os.system('ls>ls')
  output = subprocess.check_output(['ls'])
  bot.send_message(message.chat.id,output)

@bot.message_handler(commands=['kolya'])
def kolya(message):
  bot.send_message(message.chat.id, 'https://name.kamakepar.ru/request.pdf')


@bot.message_handler(content_types=['text'])
def lalala(message):
  if (message.text == 'Hello'):
    bot.send_message(message.chat.id, 'Hello Man')
  else:
    u = 'Your message was: '+str(message.text)+' :-)'
    bot.send_message(message.chat.id, u)
bot.polling(none_stop=True)
