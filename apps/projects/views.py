from rest_framework import generics
from .models import Banner, Videos, Music, Books, TextBooks
from .serializers import BannerSerializer, VideosSerializer, MusicSerializer, BooksSerializer, TextBooksSerializer

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True).order_by('-id')

class VideosListView(generics.ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

class VideoDetailView(generics.RetrieveAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

class MusicListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDetailView(generics.RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class BooksListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksDetailView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class TextBooksListView(generics.ListAPIView):
    queryset = TextBooks.objects.all()
    serializer_class = TextBooksSerializer

class TextBooksDetailView(generics.RetrieveAPIView):
    queryset = TextBooks.objects.all()
    serializer_class = TextBooksSerializer
