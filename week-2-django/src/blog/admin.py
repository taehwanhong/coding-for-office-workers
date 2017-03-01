from django.contrib import admin
<<<<<<< HEAD
from .models import Article
from .models import Comment
# Register your models here.

@admin.register(Article)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    pass

