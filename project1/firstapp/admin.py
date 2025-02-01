from django.contrib import admin
from .models import Aeroplane
from .models import Aero_review,Pilots, Blackbox, Aeroplane

# Register your models here.


class ReviewInline(admin.TabularInline):
    model=Aero_review
    extra=2

class AeroplaneAdmin(admin.ModelAdmin):
    list_display=('name','added_time','choices')
    inlines=[ReviewInline]


class PilotsAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('aeroplanes',)

class BlackboxAdmin(admin.ModelAdmin):
    list_display=('blackbox','black_id')


admin.site.register(Aeroplane,AeroplaneAdmin)
admin.site.register(Pilots,PilotsAdmin)
admin.site.register(Blackbox,BlackboxAdmin)