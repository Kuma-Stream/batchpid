import os
from telethon import TelegramClient

api_id = '26796802' #os.environ.get('API_ID')
api_hash = 'b8cc96196eb105c33d8ce193e5efff5c'  #os.environ.get('API_HASH')
bot_token = '5571017677:AAFCkd8w6HhgkLP3e0p53RRIVLqJLVQxn3I' #os.environ.get('BOT_TOKEN')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
