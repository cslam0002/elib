from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def manage(request):
    return render(request, 'pages/manage.html')

def books(request):
    return render(request, 'pages/books.html')

def accounts(request):
    return render(request, 'pages/accounts.html')
