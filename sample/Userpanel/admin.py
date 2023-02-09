from django.contrib import admin

# Register your models here.
from . models import Userrecord, ViewMark, UserMark

admin.site.register(Userrecord)
admin.site.register(UserMark)
admin.site.register(ViewMark)
