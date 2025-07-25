from rest_framework import serializers
from .models import Banner,Videos, Music, Books, TextBooks

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'
    
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class TextBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBooks
        fields = '__all__'
    