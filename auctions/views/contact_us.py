from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from auctions.forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                f"Message from {name}",
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return redirect('contact_success')

    else:
        form = ContactForm()

    return render(request, 'auctions/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'auctions/contact_success.html')