from django.contrib import admin

from users.models import Comment
from .models import Doctor
from .models import Appointments
from .models import Time



class DoctorsInfo(admin.ModelAdmin):
    list_display = ["name", "profession"]
    search_fields = ['name', 'profession']


class AppointmentInfo(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Doctor, DoctorsInfo)
admin.site.register(Appointments, AppointmentInfo)
admin.site.register(Comment)
admin.site.register(Time)
