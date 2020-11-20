# -*- coding: utf-8 -*-
import telebot
import config
import subprocess
import os
import requests as r
import sys

#reload(sys)
#sys.setdefaultencoding('utf8')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
  keyboard = telebot.types.ReplyKeyboardMarkup(True)
  keyboard.row('🆔 Account', '👭 Referral')
  keyboard.row('📤 Withdraw','✅ About bot')
  keyboard.row('🆘 Support')
  bot.send_message(message.chat.id,config.startmessage)
  bot.send_message(message.chat.id,'Something is wrong', reply_markup=keyboard)

  

@bot.message_handler(content_types=['text'])
def lalala(message):
  if (message.text == 'Hello'):
    bot.send_message(message.chat.id, 'Hello Man')
  else:
    u = 'Your message was: '+str(message.text)+' :-)'
    bot.send_message(message.chat.id, u)

try:
  bot.polling(none_stop=True)
  pass
except:
  pass
