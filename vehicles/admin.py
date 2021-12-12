from django.contrib import admin

from vehicles.models import Vehicle


@admin.register(Vehicle)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
