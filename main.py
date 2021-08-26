import telegram
from telegram import Update, Bot
from telegram.ext import MessageHandler, Updater, CommandHandler, CallbackContext
import requests
import re
bot = telegram.Bot(token="1979535666:AAENGjjo0OXFF7-_5ne5EnMhcJZvfhkf6Yk")
def get_url():
    contents = requests.get('https://api.thecatapi.com/v1/images/search').json()
    image_url = contents[0]['url']
    return image_url

# def get_image_url():
#     allowed_extension = ['jpg','jpeg','png']
#     file_extension = ''
#     while file_extension not in allowed_extension:
#         url = get_url()
#         file_extension = re.search("([^.]*)$",url).group(1).lower()
#     return url

def boop(update: Update, context: CallbackContext):
    url=get_url()
    bot.send_photo(update.effective_message.chat_id, photo=url)

def main():
    updater = Updater('xxxx', use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('boop',boop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
