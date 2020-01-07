from django import forms

from blog.models import Subscriber
from blog.models import MessageOfClients
from doctors.models import Appointments, Time
from users.models import Comment


class MessageForm(forms.Form):
    email = forms.CharField(max_length=200,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email-adress'}))

    class Meta:
        model = Subscriber
        fields = ('email',)


class MessageFormOfDoctors(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'placeholder': 'Name:'}))
    email = forms.EmailField(max_length=30,
                             widget=forms.EmailInput(attrs={'placeholder': 'E-mail:'}))
    subject = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'placeholder': 'Subject:'}))
    message = forms.CharField(max_length=300,
                              widget=forms.Textarea(attrs={'placeholder': 'Message:'}))

    class Meta:
        model = MessageOfClients
        fields = ('name', 'email', 'subject', 'message')


class AppointmentsForm(forms.ModelForm):
    doctor = forms.CharField(max_length=50)

    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'placeholder': 'Name:'}))
    email = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'placeholder': 'E-mail:'}))
    date = forms.CharField(max_length=30,
                           widget=forms.DateInput(
                               attrs={'id': 'date', 'type': 'date', 'class': 'forma', 'name': 'date'}))
    time = forms.CharField(max_length=30,
                           widget=forms.TimeInput(
                               attrs={'id': 'time', 'type': 'time', 'class': 'forma', 'name': 'time'}))

    class Meta:
        model = Appointments
        fields = ('doctor', 'name', 'email', 'date', 'time')


class TimeForm(forms.ModelForm):
    monday_am = forms.CharField(max_length=10,
                                widget=forms.TimeInput(
                                    attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    monday_pm = forms.CharField(max_length=10,
                                widget=forms.TimeInput(
                                    attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    tuesday_am = forms.CharField(max_length=10,
                                 widget=forms.TimeInput(
                                     attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    tuesday_pm = forms.CharField(max_length=10,
                                 widget=forms.TimeInput(
                                     attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    wednesday_am = forms.CharField(max_length=10,
                                   widget=forms.TimeInput(
                                       attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    wednesday_pm = forms.CharField(max_length=10,
                                   widget=forms.TimeInput(
                                       attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    thursday_am = forms.CharField(max_length=10,
                                  widget=forms.TimeInput(
                                      attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    thursday_pm = forms.CharField(max_length=10,
                                  widget=forms.TimeInput(
                                      attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    friday_am = forms.CharField(max_length=10,
                                widget=forms.TimeInput(
                                    attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    friday_pm = forms.CharField(max_length=10,
                                widget=forms.TimeInput(
                                    attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    saturday_am = forms.CharField(max_length=10,
                                  widget=forms.TimeInput(
                                      attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    saturday_pm = forms.CharField(max_length=10,
                                  widget=forms.TimeInput(
                                      attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    sunday_am = forms.CharField(max_length=10,
                                widget=forms.TimeInput(
                                    attrs={'id': 'time', 'type': 'time', 'name': 'time'}))
    sunday_pm = forms.CharField(max_length=10,
                                widget=forms.TimeInput(
                                    attrs={'id': 'time', 'type': 'time', 'name': 'time'}))

    class Meta:
        model = Time
        fields = (
            'monday_am', 'monday_pm', 'tuesday_am', 'tuesday_pm', 'wednesday_am', 'wednesday_pm', 'thursday_am',
            'thursday_pm',
            'friday_am', 'friday_pm', 'saturday_am', 'saturday_pm', 'sunday_am', 'sunday_pm')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class TimeUpdateForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['monday_am', 'monday_pm', 'tuesday_am', 'tuesday_pm', 'wednesday_am', 'wednesday_pm', 'thursday_am',
                  'thursday_pm', 'friday_am', 'friday_pm', 'saturday_am', 'saturday_pm', 'sunday_am', 'sunday_pm']
