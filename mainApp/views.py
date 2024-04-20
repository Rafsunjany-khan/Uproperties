from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

def properties(request):
    return render(request, 'properties.html')

def blog(request):
    return render(request, 'blog.html')

def service(request):
    return render(request, 'services.html')

def addProperties(request):
    return render(request, 'add-properties.html')
