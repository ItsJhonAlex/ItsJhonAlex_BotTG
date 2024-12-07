from telegram import Update
from telegram.ext import ContextTypes
from src.bot.decorators.auth_decorator import authorized_users_only

@authorized_users_only
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Envíame cualquier mensaje y lo publicaré en el canal en español e inglés."
    )
