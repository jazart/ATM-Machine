
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
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
            'content': " today is " + datetime.datetime.now().strftime("%A, %d, %b, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "ATM/about.html",
        {
            'title': "About the ATM",
           
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
    #dummy()
    #test()
    if request.method == 'POST':

        if(Account.objects.filter(num = request.POST.get('accnum')).count() == 0):
            print("test")
            user = User(name = request.POST.get('name'))
            account = Account(num =  request.POST.get('accnum'), phonenum = "7069574826", name = request.POST.get('name'), 
                              balance = 0.00, owner = user, account_type = "Savings")
            user.save()
            account.save()
        
        ATMCard.objects.create(
            name = request.POST.get('name'),
            account = Account.objects.filter(name = request.POST.get('name')).first(),
            dateofissue = request.POST.get('dateissue'),
            expiration = request.POST.get('expdate'),
            num = request.POST.get('cardnum'),
            pin = request.POST.get('pin'),
        )
    #for card in ATMCard.objects.all():
    #    print("Info: {num}, {name}, {pin}".format(num = card.num, name = card.name, pin = card.pin))


    return render(request, "ATM/admin.html", {'title': "ATM Card", 'content' : "This page will display the status of the ATM"})

#def test():
#    print(Account.objects.all()[0].name)
def dummy():
    ##User.objects.create(name="Kendrick")
    user = User.objects.all()[0]
    user.name  = "Kendrick Gholston"
    user.save()
    ##account = Account(num = "6784567898", phonenum = "7069574826", name = "Kendrick Gholston", balance = 5000.78, owner = user, account_type = "Savings")
    ##account.save()

def request_page(request):
    if(request.POST.get('content')):
        print("Saving Atm")
        new_atm = ATM(num=(int(request.POST.get('content'))))
        new_atm.save()
    return HttpResponseRedirect('/home/')

def portal(request):
    return render(request, "ATM/portal.html", {'user': "User Mode", 'admin' : "Admin Mode"})


def status(request):
    ATM.objects.all().delete()
    dummyA()
    atmStat = ATM.objects.all()

    return render(request, "ATM/status.html", {'atms' : atmStat})

def dummyA():
    atm = ATM(address = "4395 university ave", Lrefill = datetime.datetime.now(), Minbalance = 324342.66, NrefillDate = datetime.date(2019,1,18), balance = 2423423.66)
    atm.save()
    atm2 = ATM(address = "7800 schomburg rd", Lrefill = datetime.datetime.now(), Minbalance = 324342.66, NrefillDate = datetime.date(2019,1,18), balance = 1003423.70)
    atm2.save()
