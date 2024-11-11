#source bot_env/bin/activate
# sudo -H python3 -m pip install "celery[redis]" --upgrade 
# pip show python-telegram-bot
# @Ech0echos_bot
# python3 -m venv env

import logging
import config
import ephem
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

msg = '🪐 А еще я могу рассказать в каком созвездии сегодня находится планета. 🪐 Введите /planet и название планеты на английском, например /planet Mars, чтобы узнать 🚀'

logging.basicConfig(
    level=logging.INFO,
    filename='bot.log',
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('Вызван /start')
    user_f_name = update.message.chat.first_name
    user_l_name = update.message.chat.last_name
    user_id = update.message.chat.id
    user_nick = update.message.chat.username
    print(f'Пришел юзер {user_f_name} {user_l_name} c id = {user_id} и username = {user_nick}')
    await update.message.reply_text(f"Привет, {user_f_name}! Вы вызвали команду /start")
    await update.message.reply_text(msg)

async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text 
    user_nick = update.message.chat.username
    print(f'Юзер {user_nick} ввел {user_text}')
    await update.message.reply_text(f'{user_text}')

async def planet_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    planet_name = update.message.text.split()[1]
    today = datetime.datetime.now()
    try:
        planet = getattr(ephem, planet_name)(today.strftime('%Y/%m/%d'))
        ephem_answer = ephem.constellation(planet)
        logging.info(planet_name)
        await update.message.reply_text(f'🌜Сегодня планета {planet_name} находится в созвездии {ephem_answer[1]}🌛')
    except AttributeError as ae:
        await update.message.reply_text(f'🌚Я не знаю такой планеты {planet_name}.🌚')
        logging.info(f'Ошибка c планетой: {ae}')
        print(f'Ошибка c планетой: {ae}')

async def main() -> None:
    try:
        app = ApplicationBuilder().token(config.TOKEN).build()

        app.add_handler(CommandHandler("start", greet_user))
        app.add_handler(CommandHandler("planet", planet_info))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me))
        
        logging.info('Бот стартовал!')
        await app.run_polling()
    except Exception as ex:
        logging.info(f'Ошибка в функции main: {ex}')
        print(f'Ошибка в функции main: {ex}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    import asyncio
    asyncio.run(main())