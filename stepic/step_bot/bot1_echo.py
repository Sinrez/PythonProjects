#source bot_env/bin/activate
# sudo -H python3 -m pip install "celery[redis]" --upgrade 
# pip show python-telegram-bot
# @Ech0echos_bot

import json
from telegram import Update
from telegram.ext import Updater, CallbackContext, TypeHandler
from config import key_for_echo 

def echo(update: Update, context: CallbackContext) -> None:
    text = json.dumps(update.to_dict(), indent=2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def main() -> None:
    updater = Updater(key_for_echo)

    updater.dispatcher.add_handler(TypeHandler(Update, echo))

    updater.start_polling()

    print('Started')

    updater.idle()


if __name__ == "__main__":
    main()