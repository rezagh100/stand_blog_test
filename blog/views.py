from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .forms import ContactUsForm
from blog.models import Article, Category


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'articles': objects_list})


def category_list(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    article = category.article_set.all()
    return render(request, 'blog/article_list.html', {'articles': article})


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm(request.POST)
    return render(request, 'blog/contactus.html', {'form': form})
