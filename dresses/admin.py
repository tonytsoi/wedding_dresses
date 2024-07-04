from django.contrib import admin
from .models import Brand, Dress, Image, Booking

# Register your models here.
admin.site.register(Brand)
admin.site.register(Dress)
admin.site.register(Image)
admin.site.register(Booking)