import telebot
from govnocod import govnocod
from getphotos import delete_photos


tele_token = ''
bot = telebot.TeleBot(token = tele_token)

@bot.message_handler(commands=['geo'])
def geo(message):
	msg = bot.send_message(message.chat.id,'Пришлите геолокацию')
	bot.register_next_step_handler(msg,get_geo)

def get_geo(message):
	bot.send_message(message.chat.id, 'Пожалуйста, ожидайте. Мой ноутбук плохо справляется с ролью сервера.')
	geo = message.location
	geo = [geo.longitude,geo.latitude]
	path = govnocod(geo)
	photo = open(path, 'rb')
	bot.send_photo(message.chat.id,photo)
	delete_photos(path[:-16])

bot.polling()
