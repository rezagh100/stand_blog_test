from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.html import format_html
from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="30px" height="30px">')


    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.author.username}"

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs=self.article.slug)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.text[0:30]
