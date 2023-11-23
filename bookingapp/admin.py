from django.contrib import admin
from .models import Hotel, Room, Client, Reservation

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Client)
admin.site.register(Reservation)