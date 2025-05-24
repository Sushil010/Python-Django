from django.contrib import admin
from .models import Airport, Flights,Passangers

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flights)
admin.site.register(Passangers)