from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import ContactUsForm
from blog.models import Article, Category, Like
from django.contrib.auth.decorators import login_required


# def article_list(request):
#     articles = Article.objects.all()
#     page_number = request.GET.get('page')
#     paginator = Paginator(articles, 2)
#     objects_list = paginator.get_page(page_number)
#     return render(request, 'blog/article_list.html', {'articles': objects_list})


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
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


# def like(request, article_id):
#     article = get_object_or_404(Article,id = article_id)
#     if request.user in Article.likes.all():
#         Article.likes.remove(request.user)

#     else:
#         Article.likes.add(request.user)

#     return redirect('')

def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(article_id = pk , user_id=request.user.id)
        
    return redirect("post:list_view")