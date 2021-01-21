from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFit,ResizeToFill,Thumbnail

class Article(models.Model):
    title=models.CharField(max_length=140)
    image=models.ImageField(blank=True)
    image_thumbnail=ImageSpecField(source='image',
                                   processors=[Thumbnail(50,50)],
                                   format='JPEG',
                                   options={'quality':60})
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='articles')



class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    content=models.TextField()

