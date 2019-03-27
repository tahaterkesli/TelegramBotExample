#!/usr/bin/env python2.7
import os

if os.path.exists("token.txt"):
	token = open("token.txt").readline().strip()
else:
	print "token not defined, exiting..."
	os._exit(0)
	
try :
	from telegram.ext import Updater
	from telegram.ext import CommandHandler, MessageHandler
except:
	os.system("sudo pip install python-telegram-bot --upgrade")
	from telegram.ext import Updater
	from telegram.ext import CommandHandler, MessageHandler
	

updater 	= Updater(token = token)
dispatcher 	= updater.dispatcher



def my_id(bot, update):
	id 	 = update.message.chat_id
	name = update.message.chat.first_name
	msg	 = "Hello {},\n Your telegram id {}".format(name, id)
	bot.sendMessage(chat_id=update.message.chat_id, text=msg)


def command(bot, update, args=None):
	name = update.message.chat.first_name
	if args:
		msg = "<b>CommandHandler Echo: </b>\n"
		msg += " ".join(args)
	else:
		msg = 	"Hello %s,\n" \
				"This is echo command.\n\n" \
				"Example: <b> /echo hello bot</b>\n" \
				"Response: <b>hello bot</b>" % name
	bot.sendMessage(chat_id=update.message.chat_id, text=msg, parse_mode="HTML")


def message(bot, update):
	name = update.message.chat.first_name
	text = update.message.text.encode("utf-8")
	msg  = "<b>MessageHandler Echo: </b>\n{}".format(text)
	bot.sendMessage(chat_id=update.message.chat_id, text=msg, parse_mode="HTML")
	
	

dispatcher.add_handler(CommandHandler("me", my_id))
dispatcher.add_handler(CommandHandler("echo", command, pass_args=True))
dispatcher.add_handler(MessageHandler("", message))

# start bot
updater.start_polling()



