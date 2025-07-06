import telebot
from telebot import types
import json

# Carga la información de las modelos desde el archivo JSON
with open('data/modelos_info.json', 'r') as f:
    modelos_info = json.load(f)

def handle_start(bot, message):
    markup = types.InlineKeyboardMarkup()
    for modelo in modelos_info:
        markup.add(types.InlineKeyboardButton(text=modelo, callback_data=f'modelo_{modelo}'))
    bot.send_message(message.chat.id, "Selecciona la modelo sobre la que deseas obtener información:", reply_markup=markup)
