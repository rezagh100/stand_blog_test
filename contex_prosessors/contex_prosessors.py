from blog.models import Article, Category


def recent_article(request):
    recent_article = Article.objects.order_by('-created_at')[:3]
    category = Category.objects.all()
    return {'recent_article': recent_article, 'category': category}
