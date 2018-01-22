from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import random

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('안녕하세요')

@respond_to('I love you')
def love(message):
    message.reply('에..?')

@listen_to('Can someone help me?')
def help(message):
    message.reply('네')
    #message.send('I can help everybody!')
    #message.reply("Here's a threaded reply", in_thread=True)

@respond_to('menu')
def decide_menu(message):
    reply_list = ['1', '2']
    menu = reply_list[random.randrange(0, len(reply_list))]
    message.reply("오늘 메뉴는 '%s' 어떠신가요?" % menu)