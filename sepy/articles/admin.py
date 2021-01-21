from django.contrib import admin
from .models import Article,Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','user','image','title','created_date']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
