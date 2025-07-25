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
    def __str__(self):
        return f"{self.title}-{self.is_active}"