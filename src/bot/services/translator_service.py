from deep_translator import GoogleTranslator

class TranslatorService:
    @staticmethod
    def translate_to_english(text: str) -> str:
        translator = GoogleTranslator(source='es', target='en')
        return translator.translate(text)

    @staticmethod
    def format_bilingual_message(spanish: str, english: str) -> str:
        return f"🇪🇸 Español:\n{spanish}\n\n🇬🇧 English:\n{english}"
