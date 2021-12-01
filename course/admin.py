from django.contrib import admin

from .models import Course, Event, Location

admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Location)
