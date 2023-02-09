from django.contrib import admin
from django.urls import path

from . views import markview, Userrec, Usermark

urlpatterns = [
    path('Userpanel/Userrec/', Userrec.as_view()),
    path('Userpanel/Usermark/', Usermark.as_view()),
    path('Userpanel/markview/', markview.as_view()),
]