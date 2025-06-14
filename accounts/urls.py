from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('edit', views.edit, name='edit'),
    path('listing', views.listing, name='listing'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('reset', views.reset, name='reset'),
    path('search', views.search, name='search'),
    path('update', views.update, name='update'),

]
