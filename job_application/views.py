from django.shortcuts import render
from .forms import  ApplicationForm  # the forms module is locally and therefore we add "." before forms
from .models import Form
from django.contrib import messages

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
            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")


