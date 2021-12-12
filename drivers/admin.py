from django.contrib import admin

from drivers.models import Driver


@admin.register(Driver)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_at', 'updated_at']
