from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponse
from blog.models import Article, Comment
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView, CreateView
from .models import Message
from .froms import SendMessageForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'home/home.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        text = request.POST.get('text')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(text=text, article=article,
                               user=request.user, parent_id=parent_id)

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


class SendMessageView(FormView):
    form_class = SendMessageForm
    template_name = 'home/send_message.html'
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)


class MessageView(CreateView):
    model = Message
    fields = '__all__'
    template_name = 'home/send_message.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
