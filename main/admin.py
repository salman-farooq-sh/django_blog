from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import BlogPost


class BlogPostAdmin(ModelAdmin):
    list_display = ['title', 'publication_date', 'author']
    search_fields = ['title', 'body', 'author']
    list_filter = ['publication_date', 'author']
    ordering = ['-publication_date']


admin.site.register(BlogPost, BlogPostAdmin)
