from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from src.config.settings import BOT_TOKEN
from src.bot.handlers.command_handlers import start_command
from src.bot.handlers.message_handlers import handle_message

def main():
    # Crear la aplicación
    application = Application.builder().token(BOT_TOKEN).build()

    # Agregar manejadores
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar el bot
    print("Bot iniciado...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
