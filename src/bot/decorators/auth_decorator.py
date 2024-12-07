from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from src.config.settings import AUTHORIZED_USERS

def authorized_users_only(func):
    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in AUTHORIZED_USERS:
            await update.message.reply_text(
                "Lo siento, no estás autorizado para usar este bot."
            )
            return
        return await func(update, context, *args, **kwargs)
    return wrapped
