from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'webpages/index.html')


def about(request):
    return render(request, 'webpages/about.html')

def hospital(request):
    return render(request, 'webpages/hospital.html')

def service(request):
    return render(request, 'webpages/service.html')

def contact(request):
    return render(request, 'webpages/contact.html')

def login(request):
    return render(request, 'webpages/login.html')

def signup(request):
    return render(request, 'webpages/signup.html')



   

