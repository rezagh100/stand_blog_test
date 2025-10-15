from turtle import mode
from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_image', 'author')
    list_filter = ('title',)
    search_fields = ('title', 'body')

#hi
admin.site.register(models.Like)
