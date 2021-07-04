# telegram_forward_message_bot
This bot forward messages on chat

config.py <br>

BOT_TOKEN: @BotFather generate

OWNER_CHAT_ID:  run this bot and send /start chat_id printed on chat<br>

CHAT_LIST: the list of chats to which you want to forward messages

<h2>How does this work</h2>
pip install -r requirements.txt

setup config.py

python bot_functions.py

add this bot to the chats to which you want to send messages.
write /start and add chat_id in config.CHAT_LIST

restart the bot

Now all messages that you write to this bot will be redirected to all chats from the specified list.