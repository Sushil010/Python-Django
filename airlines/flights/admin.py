from django.contrib import admin
from .models import Airport, Flights,Passangers

# Register your models here.
class FlightModels(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassangerDisplay(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Airport)
admin.site.register(Flights,FlightModels)
admin.site.register(Passangers,PassangerDisplay)