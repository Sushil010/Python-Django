from django.contrib import admin
from .models import Aeroplane
from .models import Aero_review,Pilots,Blackbox

# Register your models here.
admin.site.register(Aeroplane)

class ReviewInline(admin.TabularInline):
    model=Aero_review
    extra=2

class AeroplaneAdmin(admin.ModelAdmin):
    list_display=('name','added_time','choices')
