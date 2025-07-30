from rest_framework import serializers
from .models import Banner,Videos, Music, Books, TextBooks, Category, Documents

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
        read_only_fields = ('is_favorite','title', 'description','audio')
        


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class TextBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBooks
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'