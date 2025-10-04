from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:slug>', views.article_detail, name='detail'),
    path('search/', views.search, name='search'),
    path('test/', views.ListView.as_view(), name='test'),
]
