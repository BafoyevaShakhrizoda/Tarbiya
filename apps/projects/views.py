from rest_framework import generics
from .models import Banner, Videos, Music, Books, TextBooks, Category
from .serializers import (BannerSerializer, VideosSerializer,
                          MusicSerializer, BooksSerializer, 
                          TextBooksSerializer, CategorySerializer
                          )
from rest_framework.views import APIView
from rest_framework.response import Response

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

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_queryset(self):
        name= self.request.query_params.get('name')
        return self.queryset.filter(name=name)

class Search(APIView):
    def get(self, request):
        query = request.query_params.get('name')
        category= request.query_params.get('category')
        if not request.query_params:
            return Response({"error": "Please provide a search query."}, status=400)
        books= Books.objects.filter(title__icontains=query)
        videos = Videos.objects.filter(title__icontains=query)
        music = Music.objects.filter(title__icontains=query)
        textbooks = TextBooks.objects.filter(title__icontains=query)
        if not category or category == 'all':
            results = [
                {'category': 'books', 'items': BooksSerializer(books, many=True).data},
                {'category': 'videos', 'items': VideosSerializer(videos, many=True).data},
                {'category': 'music', 'items': MusicSerializer(music, many=True).data},
                {'category': 'textbooks', 'items': TextBooksSerializer(textbooks, many=True).data}
            ]
            return Response(results)
        elif category == 'books': 
            return Response(BooksSerializer(books, many=True).data)
        elif category == 'videos':
            return Response(VideosSerializer(videos, many=True).data)
        elif category == 'music':
            return Response(MusicSerializer(music, many=True).data)
        elif category == 'textbooks':
            return Response(TextBooksSerializer(textbooks, many=True).data)
        return Response({"error": "Invalid category."}, status=400)

        
            
            
        
