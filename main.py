import telebot
import config
import subprocess
import os
import urllib2

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
  u = 'http://name.kamakepar.ru/bot.php?a='+message
  page = urllib.request.urlopen(u)
  bot.send_message(message.chat.id, page.read())

bot.polling(none_stop=True)
