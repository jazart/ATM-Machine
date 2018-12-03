
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import ATM
from .models import ATMCard

def index(request):
    if request.POST.get('user'):
        mode = "User"
    elif request.POST.get('admin'): 
        mode = "Admin"
    else:
        mode = ""
    return render(request,
        "ATM/index.html",
        {
            'Title': "ATM Account Manager",
            'mode': mode,
            'message': 'Hey ' + mode,
            'content': " today is " + datetime.now().strftime("%A, %d, %b, %Y at %X")
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
    return render(request, "ATM/atm.html", {'all_atms': "kk"})


def admin(request):
    ###all_atmcards = ATMCard.objects.all()
    print(request.POST.get('name'))
    #if reques.POST:
    #    ATMCard.objects.create(
    #        ## get fields here and assign them
    #        ## or you can just pass the entire dict
    #        # pass in "request.POST"
    #        )
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
    ##ATM.objects.all().delete()
    ##dummy()

    atmStat = ATM.objects.all()
    return render(request, "ATM/status.html", {'atms' : atmStat})

def dummy():
    atm = ATM(address = "4395 university ave", Lrefill = datetime.now(), Minbalance = 324342.66, NrefillDate = datetime.now(), balance = 2423423.66)
    atm.save()
