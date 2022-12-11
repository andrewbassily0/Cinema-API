from django.contrib import admin
from .models import Guest, Movies, Reservation

# Register your models here.
admin.site.register(Guest)
admin.site.register(Movies)
admin.site.register(Reservation)

