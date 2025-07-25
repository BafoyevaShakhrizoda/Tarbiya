from modeltranslation.translator import translator, TranslationOptions
from .models import Banner

class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_text')

translator.register(Banner, BannerTranslationOptions)