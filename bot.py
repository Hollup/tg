import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
