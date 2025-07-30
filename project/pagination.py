from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class BookPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
class MusicPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size' 
    max_page_size = 100
class TextBookPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class DocumentPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

