import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8026170723:AAE-7Siap9P4OYmHQQy40L3Q67KW8BBK9pg"
bot = telebot.TeleBot(BOT_TOKEN)


WEB_APP_URL = "localhost"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    web_app_btn = InlineKeyboardButton(
        text="🎓 Открыть College App",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_btn)
    
    welcome_text = f"""
🎓 *Добро пожаловать в IT Платформа Web App!*

Нажмите кнопку ниже, чтобы открыть современный интерфейс:

✨ *В Web App доступно:*
• 📅 Расписание пар на неделю
• 📚 Учебные материалы
• 👤 Личный кабинет
• 🎨 Красивый дизайн
• 📱 Удобный интерфейс

*Ссылка:* {WEB_APP_URL}
"""
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode='Markdown',
        reply_markup=keyboard
    )

@bot.message_handler(commands=['app'])
def send_app(message):
    keyboard = InlineKeyboardMarkup()
    web_app_btn = InlineKeyboardButton(
        text="📲 Открыть College App",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_btn)
    
    bot.send_message(
        message.chat.id,
        "Нажмите кнопку чтобы открыть Web App:",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    print("🤖 Бот для Web App запущен!")
    print(f"🌐 Web App URL: {#}")
    bot.infinity_polling()
