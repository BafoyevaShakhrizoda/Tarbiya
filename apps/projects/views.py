from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
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


class SearchView(APIView):
    def get(self, request):
        content_type = request.query_params.get('type','').lower()  # not query.params
        query = request.query_params.get('query', '')     # fixed typo

        if not query:
            return Response({'error': 'Query is required'}, status=400)

        result = {}

        if content_type == 'books':
            books = Books.objects.filter(title__icontains=query)  # fixed __icontains
            result['books'] = BooksSerializer(books, many=True).data

        elif content_type == 'textbooks':
            textbooks = TextBooks.objects.filter(title__icontains=query)
            result['textbooks'] = TextBooksSerializer(textbooks, many=True).data

        elif content_type == 'music':
            music = Music.objects.filter(title__icontains=query)  # fixed model
            result['music'] = MusicSerializer(music, many=True).data

        elif content_type == 'videos':
            videos = Videos.objects.filter(title__icontains=query)
            result['videos'] = VideosSerializer(videos, many=True).data

        elif content_type is None:
            books = Books.objects.filter(title__icontains=query)
            textbooks = TextBooks.objects.filter(title__icontains=query)
            music = Music.objects.filter(title__icontains=query)
            videos = Videos.objects.filter(title__icontains=query)

            if books.exists():
              result['books'] = BooksSerializer(books, many=True).data
            if textbooks.exists():
               result['textbooks'] = TextBooksSerializer(textbooks, many=True).data
            if music.exists():                
                result['music'] = MusicSerializer(music, many=True).data
            if videos.exists():
               result['videos'] = VideosSerializer(videos, many=True).data
        else:
            return Response({'error': 'Invalid type. Must be one of: books, textbooks, music, videos'}, status=400)
       
        if result:
            return Response(result, status=status.HTTP_200_OK)    
            
        return Response({'error':'No record found'},status=400)