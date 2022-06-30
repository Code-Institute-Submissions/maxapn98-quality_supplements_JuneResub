import os

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        contact_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "subject": request.POST["subject"],
            "message": request.POST["message"],
        }

        form = ContactForm(contact_data)

        if form.is_valid():
            try:
                send_mail(contact_data["subject"], contact_data["message"], contact_data["email"],
                          [os.environ.get("EMAIL_HOST_USER")])
                form.save()
                messages.success(request, 'Message sent!')
            except BadHeaderError:
                messages.warning(request, 'Oops, something went wrong...')
                return HttpResponse('Invalid header found!')

            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)