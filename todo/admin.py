from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_at", "completed"]
    list_display_links = ["title", "created_at"]
    list_filter = ["created_at", "title", "date"]
    search_fields = ["title", "description"]