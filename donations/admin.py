from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'event_time', 'location')  # Columns to display in the admin list view
    search_fields = ('title', 'location')  # Enable search functionality
    list_filter = ('event_date', 'location')  # Filters to narrow down the list view

admin.site.register(Event, EventAdmin)
