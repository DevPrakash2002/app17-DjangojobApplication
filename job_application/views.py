from django.shortcuts import render
from .form import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
def index(requests):
    if requests.method == 'POST':
        form = ApplicationForm(requests.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            messages_body = f"""
            A new job Application was submitted . Thankyou, {first_name}
            """
            email_message = EmailMessage("Form Submitted confirmation", messages_body, to=[email])
            email_message.send()

            messages.success(requests, 'form Submitted successfully')
    return render(requests, "index.html")


def about(requests):
    return render(requests, "about.html")
