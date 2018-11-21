"""
Definition of urls for ATM_Machine.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import ATM.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', ATM.views.index, name='index'),
    url(r'^home$', ATM.views.index, name='home'),
    url(r'^about$', ATM.views.about, name='about'),
    url(r'^atm$', ATM.views.atm, name='ATMs')
]
