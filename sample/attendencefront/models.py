from django.db import models

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

"""
class UserReg(models.Model):
    id = models.CharField(max_length=11, primary_key=True),
    contact = models.CharField(max_length=15, null=True),
    email = models.CharField(max_length=80, null=True),
    password = models.CharField(max_length=80, null=True),

class UserLogin(models.Model):
    email = models.CharField(max_length=80, null=True),
    password = models.CharField(max_length=80, null=True),"""

class Userrecord(models.Model):
    Gender = (
        ('male', 'male'),
        ('female', 'female')
    )
    id = models.CharField(max_length=11, primary_key=True),
    name = models.CharField(max_length=25, null=True),
    gender = models.CharField(max_length=20, null=True, default=1, choices=Gender),
    age = models.CharField(max_length=19, null=True),
    contact = models.CharField(max_length=15, null=True),
    email = models.CharField(max_length=80, null=True),
    password = models.CharField(max_length=80, null=True),
    profile = models.FileField()
class UserMark(models.Model):
    mark = (
        ('present','present'),
        ('absent', 'absent'),
        ('leave request', 'leave request'),
    )

    id = models.CharField(max_length=50, primary_key=True),
    markattendence = models.CharField(max_length=50, null=True, default=1, choices=mark)

class ViewMark(models.Model):
    id = models.CharField(max_length=50, primary_key=True),


""" id = models.ForeignKey(Userrecord, null=False)
    viewmark = models.ForeignKey(UserMark, null=True)"""
