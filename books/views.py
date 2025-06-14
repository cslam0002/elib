from django.shortcuts import render

# Create your views here.

def add(request):
    return render(request, 'books/add.html')

def edit(request):
    return render(request, 'books/edit.html')

def listing(request):
    return render(request, 'books/listing.html')

def search(request):
    return render(request, 'books/search.html')