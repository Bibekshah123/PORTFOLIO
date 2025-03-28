from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def projects(request):
    return render(request, 'projects.html')

def skills(request):
    return render(request, 'skills.html')
