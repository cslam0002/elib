from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('search', views.search, name='search'),
    path('listing', views.listing, name='listing'),
    path('edit', views.edit, name='edit'),
    path('add', views.add, name='add'),

]
