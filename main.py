import telebot
import config
import subprocess
import os
import urllib2
import urllib.request

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
  if (message == 'Hello'):
    bot.send_message(message.chat.id, 'Hello Man')
  else:
    u = 'Your message was: '+str(message)+' :-)'
    bot.send_message(message.chat.id, u)
bot.polling(none_stop=True)
