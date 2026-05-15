from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def home(request):
    return render(request, 'home.html')

def self_help(request):
    return render(request, 'self_help.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def hours(request):
    return render(request, 'hours.html')

def book_service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_success')
    else:
        form = ServiceRequestForm()

    return render(request, 'book_service.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def request_success(request):
    return render(request, 'request_success.html')

def faq(request):
    return render(request, 'faq.html')