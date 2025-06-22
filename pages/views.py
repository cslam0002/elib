from django.shortcuts import render

from books.models import Book

# Create your views here.

def index(request):
    listings = Book.objects.order_by('-date_arrived')[:5]
    context = {"listings" : listings, }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')