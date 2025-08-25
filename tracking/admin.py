from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Package, StatusUpdate

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'status', 'origin', 'destination', 'updated_at')
    search_fields = ('tracking_id', 'sender_name', 'receiver_name')

@admin.register(StatusUpdate)
class StatusUpdateAdmin(admin.ModelAdmin):
    list_display = ('package', 'location', 'timestamp')
    search_fields = ('package__tracking_id',)