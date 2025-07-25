from django.db import models
from apps.common.models import BaseModel

class Banner(BaseModel):
    title = models.CharField(max_length=255)
    description= models.TextField()
    image= models.ImageField(upload_to='posts/images/', blank=True, null=True)   
    link= models.URLField(blank=True, null=True)
    button_text= models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        if self.is_active:
            active_banners = Banner.objects.filter(is_active=True).exclude(id=self.id)
            if active_banners.count() >= 4:
                if oldest := active_banners.order_by('id').first():
                    Banner.objects.filter(id=oldest.id).update(is_active=False)

class Videos(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/')

class Music(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='music/')
    is_favorite = models.BooleanField(default=False)
    

class Books(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image= models.ImageField(upload_to='book/images/', blank=True, null=True)
    book = models.FileField(upload_to='book/books/')
    instagram_link = models.URLField(blank=True, null=True)
    twiter_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)


