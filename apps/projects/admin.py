from django.contrib import admin
from .models import Banner, Videos, Music, Books, TextBooks, Category

admin.site.register(Banner)
admin.site.register(Videos)
admin.site.register(Music)
admin.site.register(Books)
admin.site.register(TextBooks)
admin.site.register(Category)