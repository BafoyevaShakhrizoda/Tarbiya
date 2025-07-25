from django.urls import path
from apps.projects.views import( 
                                BannerListView, VideosListView,
                                VideoDetailView, MusicListView, 
                                MusicDetailView,BooksListView,
                                BooksDetailView,
)
urlpatterns = [
    path('banners/', BannerListView.as_view(), name='banner_list'),
    path('videos/', VideosListView.as_view(), name='videos_list'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='banner_detail'),
    path('music/', MusicListView.as_view(), name='music_list'),
    path('music/<int:pk>/', MusicDetailView.as_view(), name='music_detail'),
    path('books/',BooksListView.as_view(),name="book_list"),
    path("books/<int:pk>/",BooksDetailView.as_view(),name="book_detail"),
]
