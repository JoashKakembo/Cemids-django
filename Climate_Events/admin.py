from django.contrib import admin
from .models import ClimateEvent

@admin.register(ClimateEvent)
class ClimateEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'location', 'event_date', 'event_time')
    search_fields = ('event_title', 'location', 'description')
    list_filter = ('event_date', 'event_time')
