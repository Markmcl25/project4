from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'category', 'creator', 'is_published')
    list_filter = ('date', 'category', 'is_published')
    search_fields = ('title', 'location', 'description')
    ordering = ('-date',)
    list_editable = ('is_published',)

    # To ensure the creator is automatically assigned
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set creator when creating the event
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
