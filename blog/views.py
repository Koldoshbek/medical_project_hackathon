from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings

from blog.models import New
from doctors.forms import MessageForm, MessageFormOfDoctors
from doctors.models import Doctor, Appointments
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def about(request):
    doctors = User.objects.all()
    users = User.objects.all().select_related('Profile')
    form = MessageForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Thank you for registering to our site'
        message = request.POST.get('email')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'blog/about.html', {'doctors': doctors, 'form': form, 'users': users})



def contact(request):
    doctors = User.objects.all()
    formClientsMessage = MessageFormOfDoctors()
    if request.method == 'POST':
        subject = 'Thank you for registering to our site'
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'blog/contact.html',
                  {'doctors': doctors, 'formClientsMessage': formClientsMessage})


def elements(request):
    doctors = Doctor.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Thank you for registering to our site'
        message = request.POST.get('email')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'blog/elements.html', {'doctors': doctors, 'form': form})


def news(request):
    news = New.objects.all()
    users = User.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Thank you for registering to our site'
        message = request.POST.get('email')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'blog/news.html', {'form': form, 'news': news, 'users': users})


class PostListView(ListView):
    model = New
    template_name = 'blog/news.html'
    context_object_name = 'news'


class PostDetailView(DetailView):
    model = New


class PostCreateView(LoginRequiredMixin, CreateView):
    model = New
    fields = ['subject', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = New
    fields = ['subject', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = New
    success_url = '/news'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def services(request):
    doctors = Doctor.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Thank you for registering to our site'
        message = request.POST.get('email')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'blog/services.html', {'doctors': doctors, 'form': form})

# def getNews(request, index_id):
#     news = New.objects.get(id=index_id)
#     return render(request, 'blog/getNews.html', {'news': news})
