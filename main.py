import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from requests import get


def retrieve_IP_address():
    body = get('http://checkip.dyndns.org').content.decode('utf8')
    ip = body.split('Address:')[1].split('<')[0]
    return ip

async def start_callback(update, context):
    await update.message.reply_text('La commande est /getIp')

async def get_IP_callback(update, context):
    await update.message.reply_text(f'L\'adresse IP du serveur est: {retrieve_IP_address()}')

def main():
    load_dotenv()

    BOT_TOKEN = os.getenv('BOT_TOKEN')
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start_callback))
    application.add_handler(CommandHandler('getIp', get_IP_callback))
    application.run_polling()


if __name__ == '__main__':
    main()