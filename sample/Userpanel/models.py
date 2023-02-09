import stat

from django.db import models

"""
User panel:

User panel may include the registration page, and login
There must be a 3 buttons , mark attendance , Mark Leave and view button
Mark attendance in which students can mark his/her attendance as present
View button in which student can view all the marked attendance
Student which mark his/her attendance once in a day can’t mark it again in as well as not delete his/her attendance.
Also give the option to edit the profile picture
User should be able to Send Leave Request to admin for leaves.
"""
# Create your models here.
#registration and login front end design i will backend ready
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