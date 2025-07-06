import telebot
from config import TOKEN
from handlers import start_handler, message_handler

# Crea una instancia del bot
bot = telebot.TeleBot(TOKEN)

# Registro de manejadores
@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler.handle_start(bot, message)

@bot.callback_query_handler(func=lambda call: call.data.startswith('modelo_'))
def handle_modelo_selection(call):
    message_handler.handle_modelo_selection(bot, call)

@bot.callback_query_handler(func=lambda call: call.data.startswith('info_'))
def handle_info_request(call):
    message_handler.handle_info_request(bot, call)

# Inicia el bot
bot.polling()
