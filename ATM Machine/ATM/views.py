
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import ATM, ATMCard, Account, User

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
    #print(request.POST.get('name'))
    #if reques.POST:
    #User.objects.create(name="Kendrick")
    #user = User.objects.all()[0]
    if request.method == 'POST':
        ATMCard.objects.create(
            name = request.POST.get('name'),
            account = Account.objects.all()[0],
            dateofissue = request.POST.get('dateissue'),
            expiration = request.POST.get('expdate'),
            num = request.POST.get('cardnum'),
            pin = request.POST.get('pin'),
        )
    #for card in ATMCard.objects.all():
    #    print("Info: {num}, {name}, {pin}".format(num = card.num, name = card.name, pin = card.pin))


    return render(request, "ATM/admin.html", {'title': "ATM Status", 'content' : "This page will display the status of the ATM"})

def dummy():
    account = Account(num = "6784567898", phonenum = "7069574826", name = "Kendrick Gholston", balance = 5000.78)
    account.save()

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


