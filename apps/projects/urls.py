from django.urls import path
from apps.projects.views import BannerListView

urlpatterns = [
    path('banners/', BannerListView.as_view(), name='banner_list'),
]
