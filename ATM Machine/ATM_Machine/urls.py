"""
Definition of urls for ATM_Machine.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path
import django.contrib.auth.views

import ATM.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', ATM.views.portal),
    path('home/', ATM.views.index, name='home'),
    path('about/', ATM.views.about, name='about'),
    path('atm/', ATM.views.atm, name='ATMs'),
    path('status/', ATM.views.status, name='status'),
    path('request_page/', ATM.views.request_page),
    path('admin/', ATM.views.admin, name = "admin")
]
