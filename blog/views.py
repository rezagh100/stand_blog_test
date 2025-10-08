from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from .forms import ContactUsForm
from blog.models import Article, Category


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'articles': objects_list})



class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 1
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['articles'] = Article.objects.all()
        return context



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
