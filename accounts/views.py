from django.shortcuts import render

# Create your views here.

def edit(request):
    return render(request, 'accounts/edit.html')

def listing(request):
    return render(request, 'accounts/listing.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'pages/index.html')

def register(request):
    return render(request, 'accounts/register.html')

def reset(request):
    return render(request, 'accounts/reset.html')

def search(request):
    return render(request, 'accounts/search.html')

def update(request):
    return render(request, 'accounts/update.html')