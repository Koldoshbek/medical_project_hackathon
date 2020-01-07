from django.contrib import admin

from .models import Subscriber
from .models import MessageOfClients
from .models import New

admin.site.register(Subscriber)
admin.site.register(MessageOfClients)
admin.site.register(New)

