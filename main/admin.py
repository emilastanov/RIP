from django.contrib import admin
from . import models

admin.site.site_header = "Мой список дел"

@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Events)
class EventsAdmin(admin.ModelAdmin):
    pass