from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from mailjet_rest import Client
from decouple import config
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/index.html")
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        country = request.POST.get("country")
        occupation = request.POST.get("occupation")
        marital_status = request.POST.get("marital_status")
        loan_amount = request.POST.get("loan_amount")
        loan_type = request.POST.get("loan_type")
        loan_duration = request.POST.get("loan_duration")
        monthly_income = request.POST.get("monthly_income")

        #Sending mail
        subject = 'Loan Application'
        message = f'''
            NAME: {name} \n
            EMAIL: {email} \n
            PHONE: {phone} \n
            DATE OF BIRTH: {dob} \n
            ADDRESS: {address} \n
            COUNTRY: {country} \n
            OCCUPATION: {occupation} \n
            MARITAL STATUS: {marital_status} \n
            LOAN AMOUNT: {loan_amount} \n
            PURPOSE OF LOAN: {loan_type} \n
            LOAN DURATION: {loan_duration} \n
            MONTHLY INCOME: {monthly_income}
        '''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["loans@cravitzgroup.com", ]
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request, 'Loan Application Succesful. Your Application will be reviewed and response will be sent to you. Thank You.')
        return redirect('.')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/about.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/contact-us.html")


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/services.html")


class NewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/news.html")