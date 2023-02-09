from django.db import models


"""
Admin panel:

The admin can login through login page
View all the record of login students
The admin can edit, add, and delete the students attendance
Admin should be able to create a report of Users. FROM  and TO Dates which will show specific user attendance
Leave Approval Modules. There should be proper count of Leaves , Present’s  , Absents etc
Admin should be able to create a Complete System Report FROM and TO dates of all attendances
Add up grading System, if user attended 26 Days he should have A grade for other grades setting add up a module. E.g.  10 Days = D grade etc. etc. in admin panel

"""
# Create your models here.
class adminLogin(models.Model):
    id = models.CharField(max_length=50, primary_key=True),
    email = models.CharField(max_length=80, null=True),
    password = models.CharField(max_length=80, null=True),

class viewstudent(models.Model):
    adminid = models.CharField(max_length=50, primary_key=True),

"""    id = models.ForeignKey('sample.models', max_length=11, primary_key=True, on_delete=models.CASCADE()),
    name = models.ForeignKey('sample.models', max_length=25, null=True, on_delete=models.CASCADE()),"""

class userreport(models.Model):
    adminid = models.CharField(max_length=50, primary_key=True),

    Report = models.CharField(max_length=500, null=True)
"""    id = models.ForeignKey(Userpanel, max_length=11),
    name = models.ForeignKey(Userpanel, max_length=25, null=True),"""

class leaveapproval(models.Model):
    adminid = models.CharField(max_length=50, primary_key=True),

"""    id = models.ForeignKey(Userpanel, max_length=11, primary_key=True),
    name = models.ForeignKey(Userpanel, max_length=25, null=True),"""

class attendencecount(models.Model):
    id = models.CharField(max_length=50, primary_key=True),
"""    present = models.ForeignKey()
"""
class gradingsys(models.Model):
    id = models.CharField(max_length=50, primary_key=True),
    addgrade = models.CharField(max_length=50, null=True),

