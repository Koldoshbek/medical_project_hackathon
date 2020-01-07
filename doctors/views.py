from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from requests import post

from blog.models import New
from doctors.forms import MessageForm, AppointmentsForm, TimeForm, TimeUpdateForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives

from doctors.models import Appointments, Time
from django.views.generic import ListView, DeleteView
from django.db.models import Q

from users.models import Comment
from doctors.forms import CommentForm


def send(request):
    doctors = User.objects.all()
    users = User.objects.all().select_related('Profile')
    form = MessageForm()
    if request.method == 'POST':
        subject, from_email, to = 'hello', 'testingturizm@gmail.com', 'suiunalievich32@gmail.com'
        text_content = 'This is an important message.'
        html_message = render_to_string('doctors/appointment.html', {'context': 'values'})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_message, "text/html")
        msg.send()
    return render(request, 'doctors/index.html', {'doctors': doctors, 'form': form, 'users': users})


def index(request):
    doctors = User.objects.all()
    posts = New.objects.all()
    users = User.objects.all().select_related('Profile')
    form = MessageForm()
    if request.method == 'POST':
        subject = 'Thank you for registering to our site'
        html_message = render_to_string('doctors/appointment.html', {'context': 'values'})
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['suiunalievich32@gmail.com']
        send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    return render(request, 'doctors/index.html', {'doctors': doctors, 'form': form, 'users': users, 'posts': posts})


def getDoctors(request, index_id):
    doctors = User.objects.get(id=index_id)
    app = Appointments.objects.all()
    forma = AppointmentsForm(request.POST)
    time = Time.objects.all()
    if forma.is_valid():
        forma.save()
        return redirect('index')
    else:
        forma = AppointmentsForm()
    return render(request, 'doctors/getDoctors.html', {'doctors': doctors, 'forma': forma, 'app': app, 'time': time})


def getInfo(request, index_id):
    doctors = User.objects.get(id=index_id)
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get('comment')
            commenta = Comment.objects.create(post=doctors, name=request.user.first_name + ' ' + request.user.last_name,
                                              comment=content)
            commenta.save()
            return render(request, 'users/doctorsInfo.html', {'form': form, 'doctors': doctors, 'comments': comments})
    else:
        form = CommentForm()
    return render(request, 'users/doctorsInfo.html', {'form': form, 'doctors': doctors, 'comments': comments})


def doctorsPage(request, index_id):
    search_query = request.GET.get('search', '')
    if search_query:
        if search_query.lower() == 'accepted':
            search_query = '1'
            clients = Appointments.objects.filter(Q(waiting__icontains=search_query))
        elif search_query.lower() == 'denied':
            search_query = '2'
            clients = Appointments.objects.filter(Q(waiting__icontains=search_query))
        elif search_query.lower() == 'waiting':
            search_query = '0'
            clients = Appointments.objects.filter(Q(waiting__icontains=search_query))

        else:
            clients = Appointments.objects.filter(
                Q(passwordId__icontains=search_query) | Q(name__icontains=search_query))
    else:
        clients = Appointments.objects.all()
    doctors = User.objects.get(id=index_id)

    return render(request, 'users/doctorsPage.html', {'doctors': doctors, 'clients': clients})


def appointments(request, index_id):
    doctors = User.objects.get(id=index_id)
    clients = Appointments.objects.all()
    return render(request, 'users/appointments.html', {'doctors': doctors, 'clients': clients})


def deny(request, index_id):
    appointment = Appointments.objects.get(id=index_id)
    appointment.waiting = 2
    appointment.save()
    return render(request, 'doctors/index.html')


def accept(request, index_id):
    appointment = Appointments.objects.get(id=index_id)
    appointment.waiting = 1
    appointment.save()
    return render(request, 'doctors/index.html')


def delete_app(request, index_id):
    u = Appointments.objects.get(id=index_id).delete()
    return render(request, 'doctors/index.html')


# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#
#     return render(request, 'users/profile.html', context)


def time(request, index_id):
    doctors = User.objects.get(id=index_id)
    forma = TimeForm()
    if request.method == 'POST':
        p_form = TimeUpdateForm(request.POST, request.FILES, instance=request.user.time)
        if p_form.is_valid():
            p_form.save()
            return redirect('index')
    else:
        p_form = TimeUpdateForm(request.POST, request.FILES, instance=request.user.time)

    return render(request, 'doctors/time.html', {'forma': forma, 'doctors': doctors, 'p_form': p_form})
