
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import ATM

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


def request_page(request):
    if(request.POST.get('content')):
        print("Saving Atm")
        new_atm = ATM(num=(int(request.POST.get('content'))))
        new_atm.save()
    return HttpResponseRedirect('/home/')