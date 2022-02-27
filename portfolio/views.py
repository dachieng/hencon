from email import message
from django.shortcuts import render
from portfolio.models import Mandate,Portfolio
from EngineerWebsite.settings import EMAIL_HOST_USER
from portfolio.forms import EmailUs
from django.core.mail import send_mail

def index(request):
    company = "Hen'Com"
    mandate = Mandate.objects.all()
    portfolio = Portfolio.objects.all()

    if request.method == "POST":
        form = EmailUs(request.POST)
        if form.is_valid():
            subject = "Welcome to Hen'Com"
            sender = form.cleaned_data.get("email")
            message = 'Hope you enjoy our services. Contact us for more information'
            send_mail(subject, 
            message, EMAIL_HOST_USER,[sender], fail_silently = False)
    else:
        form = EmailUs()
 
    return render(request,"portfolio/index.html", {"mandate":mandate,"portfolio":portfolio,"form":form,"company":company})



