from telegram import Update
from telegram.ext import ContextTypes
from src.config.settings import CHANNEL_ID
from src.bot.services.translator_service import TranslatorService
from src.bot.decorators.auth_decorator import authorized_users_only

@authorized_users_only
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje_original = update.message.text

    # Traducir y formatear el mensaje
    mensaje_en = TranslatorService.translate_to_english(mensaje_original)
    mensaje_final = TranslatorService.format_bilingual_message(mensaje_original, mensaje_en)

    # Enviar al canal
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=mensaje_final
    )

    # Confirmar al usuario
    await update.message.reply_text("¡Mensaje publicado en el canal!")
