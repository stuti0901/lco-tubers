from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'webpages/webpages/home.html')

def about(request):
    return render(request,'webpages/webpages/about.html')

def services(request):  
    return render(request,'webpages/webpages/services.html')

def contact(request):
    return render(request,'webpages/webpages/contact.html')
    
