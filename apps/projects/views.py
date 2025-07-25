from rest_framework import generics
from .models import Banner
from ..projects.serializers import BannerSerializer

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)
