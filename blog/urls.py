from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    # path('article_list', views.article_list, name='list'),
    path('category/<int:pk>', views.category_list, name='category'),
    path('contactus', views.contactus, name='contactus'),
    path('articlelist', views.ArticleListView.as_view(), name='list_view'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
    
]
