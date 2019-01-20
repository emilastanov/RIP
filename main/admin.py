from django.contrib import admin
from . import models

admin.site.site_header = "Мой список дел"

@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Events)
class EventsAdmin(admin.ModelAdmin):
    search_fields = ('event__title',)