from django.shortcuts import render, redirect
from django.core.mail import send_mail
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
            service_request = form.save()

            if service_request.email:
                send_mail(
                    subject='BEST-FIX Service Request Received',
                    message=f"""
Hi {service_request.name},

Thank you for contacting BEST-FIX.

Your service request has been received.

Request details:
Device Type: {service_request.get_device_type_display()}
Location: {service_request.location}
Best Time to Contact: {service_request.best_time_to_contact}

Issue:
{service_request.issue_description}

I will review your request and contact you with the next available appointment.

Thank you,
BEST-FIX
Computer | Phone | Wi-Fi | Printer | Website Help
""",
                    from_email=None,
                    recipient_list=[service_request.email],
                    fail_silently=False,
                )

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