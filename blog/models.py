from django.db import models
from django.utils import timezone
from django.urls import reverse


class Subscriber(models.Model):
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.email

    def contact(self):
        return ('blog/contact.html')


class MessageOfClients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=300)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.name


class New(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    text = models.TextField(max_length=1500)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
