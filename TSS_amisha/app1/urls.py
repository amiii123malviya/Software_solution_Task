from django.urls import path
from .views import *

urlpatterns=[
    path('',base,name='base'),
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('showdata/',showdata,name='showdata')
]