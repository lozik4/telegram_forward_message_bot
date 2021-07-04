import config
import telebot


bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    if int(message.chat.id) not in config.CHAT_LIST:
        bot.send_message(config.OWNER_CHAT_ID, str(message.chat.id) + ': ' +
                         f"{message.text} {message.from_user.first_name} "
                         f"{message.from_user.last_name} "
                         f"{message.from_user.username} "
                         f"{message.chat.title}")
        bot.send_message(message.chat.id, f"👍 Group registration request: {message.chat.title}, has been sent")


@bot.message_handler(content_types=["text"])
def forward_info_messages(message):
    if int(message.chat.id) == int(config.OWNER_CHAT_ID):
        try:
            text=message.text
            for chat_id in config.CHAT_LIST:
                bot.send_message(chat_id, text)
        except:
            pass

if __name__ == '__main__':
    bot.polling(none_stop=True)