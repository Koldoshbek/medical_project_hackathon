from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    information = models.TextField()
    photo = models.ImageField(upload_to='doctorsphotos', blank=True)

    def __str__(self):
        return self.name


class Appointments(models.Model):
    doctor = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    waiting = models.CharField(max_length=3, default=0)

    def __str__(self):
        return self.doctor


class Time(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    monday_am = models.CharField(max_length=10, default="09:00")
    monday_pm = models.CharField(max_length=10, default="17:00")
    tuesday_am = models.CharField(max_length=10, default="09:00")
    tuesday_pm = models.CharField(max_length=10, default="17:00")
    wednesday_am = models.CharField(max_length=10, default="09:00")
    wednesday_pm = models.CharField(max_length=10, default="17:00")
    thursday_am = models.CharField(max_length=10, default="09:00")
    thursday_pm = models.CharField(max_length=10, default="17:00")
    friday_am = models.CharField(max_length=10, default="09:00")
    friday_pm = models.CharField(max_length=10, default="17:00")
    saturday_am = models.CharField(max_length=10, default="09:00")
    saturday_pm = models.CharField(max_length=10, default="17:00")
    sunday_am = models.CharField(max_length=10, default="09:30")
    sunday_pm = models.CharField(max_length=10, default="15:00")

    def __str__(self):
        return self.author.username
