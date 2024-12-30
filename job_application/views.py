from django.shortcuts import render
from .forms import  ApplicationForm  # the forms module is locally and therefore we add "." before forms
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)  # this class we create inside job_applicaiton
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            #print(first_name)
            message_body = f"A new job application was submitted. Thank you, \n{first_name} \n{last_name}"
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")

# create for about.html to be called
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")