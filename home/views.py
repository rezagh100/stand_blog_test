from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,HttpResponse
from blog.models import Article, Comment
from django.views.generic.base import View, TemplateView

def index(request):
    articles = Article.objects.all()
    return render(request, 'home/home.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        text = request.POST.get('text')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(text=text, article=article, user=request.user, parent_id=parent_id)

    return render(request, 'home/article_detail.html', {'article': article})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'articles': objects_list})


class ListView(TemplateView):
    template_name = 'home/testlist.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
    