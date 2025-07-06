# Kinkyland Assistant Bot

Un bot de Telegram modular y eficiente diseñado para la gestión de comunidades, construido con Python y la librería `pyTelegramBotAPI`.

## ✨ Características

* **Manejo de Comandos:** Responde al comando `/start` para dar la bienvenida a los usuarios.
* **Menús Interactivos:** Utiliza botones en línea (`inline keyboards`) para guiar a los usuarios a través de selecciones, como elegir un "modelo" o solicitar información.
* **Arquitectura Modular:** El código está organizado en `handlers` separados, lo que facilita la adición de nuevas funcionalidades y el mantenimiento del bot.
* **Fácil de Configurar:** Utiliza un archivo de configuración para gestionar el token del bot de forma segura.

## 🛠️ Tecnologías Utilizadas

* **Python**
* **pyTelegramBotAPI:** Una librería de Python potente y fácil de usar para la API de bots de Telegram.

## 🚀 Instalación y Uso

Para ejecutar este bot en tu propio entorno, sigue estos pasos:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/LianBellocchio/kklassistantbot.git
   cd kklassistantbot
   ```
2. **Crea y activa un entorno virtual:**

   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```
3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configura tu token:**

   * Crea un archivo llamado `config.py`.
   * Dentro de `config.py`, añade la siguiente línea con tu propio token de BotFather:
     ```python
     TOKEN = "TU_TOKEN_DE_TELEGRAM_AQUI"
     ```
5. **Ejecuta el bot:**

   ```bash
   python bot.py
   ```

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera para asegurar la escalabilidad y mantenibilidad:

```
kklassistantbot/
├── bot.py             # Archivo principal que inicia el bot y registra los handlers
├── config.py          # (No versionado) Almacena el token del bot
├── requirements.txt   # Lista de dependencias de Python
├── handlers/          # Contiene la lógica para manejar los comandos y callbacks
│   ├── __init__.py
│   ├── start_handler.py
│   └── message_handler.py
└── ...
```
