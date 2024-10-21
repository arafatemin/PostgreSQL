from django.contrib import admin
from .models import *



class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'date_of_brith', 'country_of_brith')
admin.site.register(Person, PersonAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'price')

admin.site.register(Car, CarAdmin)
admin.site.register(Staff)
