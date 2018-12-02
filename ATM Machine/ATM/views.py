
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import ATM
from .models import ATMCard

def index(request):
    return render(request,
        "ATM/index.html",
        {
            'title': "Hello ATM!",
            'message': 'Hey ATM Machine!',
            'content': " on " + datetime.now().strftime("%A, %d, %b, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "ATM/about.html",
        {
            'title': "About the ATM",
            'content': "Exmample page for Django"
        }
     )

def atm(request):
    all_atms = ATM.objects.all()
    return render(request, "ATM/atm.html", {'all_atms': all_atms})


def admin(request):
    ###all_atmcards = ATMCard.objects.all()
    return render(request, "ATM/admin.html", {'title': "ATM Status", 'content' : "This page will display the status of the ATM"})

def request_page(request):
    if(request.POST.get('content')):
        print("Saving Atm")
        new_atm = ATM(num=(int(request.POST.get('content'))))
        new_atm.save()
    return HttpResponseRedirect('/home/')

def portal(request):
    return render(request, "ATM/portal.html", {'user': "User Mode", 'admin' : "Admin Mode"})

def status(request):
    return render(request, "ATM/status.html", {'title': "ATM Status", 'content' : "This page will display the status of the ATM"})