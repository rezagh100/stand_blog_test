from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(Article, ModelAdmin):
    list_display = ('title','body')

admin.site.register(Category)
admin.site.register(Comment)
