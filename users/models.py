from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    CLIENTS = 1
    DOCTORS = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (CLIENTS, 'Clients'),
        (DOCTORS, 'Doctors'),
        (ADMIN, 'Admin'),
    )
    MALE = 1
    FEMALE = 2
    NULL = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Famale'),
        (NULL, 'null'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='doctorsphotos/', default='doctorsphotos/foto.jpg')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=CLIENTS)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, default=NULL)
    about = models.TextField()

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.username
