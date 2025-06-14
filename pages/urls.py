from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),


    path('manage', views.manage, name='manage'),
    path('books', views.books, name='books'),
    path('accounts', views.accounts, name='accounts'),
]
