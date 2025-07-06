import json
import telebot
from telebot import types

# Carga la información de las modelos desde el archivo JSON
with open('data/modelos_info.json', 'r', encoding='utf-8') as f:
    modelos_info = json.load(f)

# Diccionario para mantener el estado del usuario
user_state = {}

def handle_modelo_selection(bot, call):
    modelo = call.data.split('_')[1]
    user_state[call.from_user.id] = modelo
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Información Básica', callback_data='info_informacion-basica'))
    markup.add(types.InlineKeyboardButton(text='Contenido Disponible', callback_data='info_contenido-disponible'))
    markup.add(types.InlineKeyboardButton(text='Agenda para Videollamadas', callback_data='info_agenda-videollamadas'))
    markup.add(types.InlineKeyboardButton(text='Tarifas', callback_data='info_tarifas'))
    markup.add(types.InlineKeyboardButton(text='No dispuesto a', callback_data='info_no-hare'))
    bot.send_message(call.message.chat.id, f"Has seleccionado a {modelo}. ¿Qué información deseas obtener?", reply_markup=markup)

def handle_info_request(bot, call):
    user_id = call.from_user.id
    if user_id in user_state:
        modelo = user_state[user_id]
        info_type = call.data.split('_')[1]
        
        # Muestra los datos de depuración
        print(f"Modelo seleccionado: {modelo}")
        print(f"Tipo de información solicitado: {info_type}")
        print(f"Datos disponibles: {modelos_info.get(modelo, {})}")
        
        info = modelos_info.get(modelo, {})
        # Asegúrate de que la clave solicitada exista en el diccionario
        response = info.get(info_type, "Información no disponible.")
        
        # Convierte la lista en una cadena si es necesario
        if isinstance(response, list):
            response = '\n'.join(response)
        
        # Asegúrate de manejar caracteres especiales
        response = response.encode('utf-8').decode('utf-8')
        
        bot.send_message(call.message.chat.id, response)
    else:
        bot.send_message(call.message.chat.id, "Por favor, selecciona una modelo primero usando el comando /start.")
