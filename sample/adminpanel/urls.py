from django.contrib import admin
from django.urls import path

from . views import grad, attenden, leaves, reportstu, adminlog, viewstud

urlpatterns = [
    path('adminpanel/adminlogin/', adminlog.as_view(), name="panel"),
    path('adminpanel/viewstud/', viewstud.as_view()),
    path('adminpanel/report/', reportstu.as_view()),
    path('adminpanel/leave/', leaves.as_view()),
    path('adminpanel/attendence/', attenden.as_view()),
    path('adminpanel/grade/', grad.as_view()),
]