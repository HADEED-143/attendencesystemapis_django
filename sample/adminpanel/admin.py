from django.contrib import admin

# Register your models here.
from .models import adminLogin, viewstudent, userreport, leaveapproval, \
    attendencecount, gradingsys

admin.site.register(adminLogin)
admin.site.register(viewstudent)
admin.site.register(userreport)
admin.site.register(leaveapproval)
admin.site.register(attendencecount)
admin.site.register(gradingsys)
