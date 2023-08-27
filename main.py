import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from requests import get

def is_authorized(update):
    CHAT_ID = os.getenv('CHAT_ID')
    return CHAT_ID == str(update.message.chat_id)

def retrieve_IP_address():
    body = get('http://checkip.dyndns.org').content.decode('utf8')
    ip = body.split('Address:')[1].split('<')[0]
    return ip

async def unauthorized_reply(update):
    await update.message.reply_text('Vous n\'avez pas les droits')

async def start_callback(update, context):
    if is_authorized(update):
        await update.message.reply_text('La commande est /getIp')
    else:
        await unauthorized_reply(update)

async def get_IP_callback(update, context):
    if is_authorized(update):
        await update.message.reply_text(f'L\'adresse IP du serveur est: {retrieve_IP_address()}')
    else:
        await unauthorized_reply(update)

def main():
    load_dotenv()

    BOT_TOKEN = os.getenv('BOT_TOKEN')
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start_callback))
    application.add_handler(CommandHandler('getIp', get_IP_callback))
    application.run_polling()


if __name__ == '__main__':
    main()