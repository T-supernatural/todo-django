from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_at", "is_completed"]
    list_display_links = ["title", "created_at"]
    list_filter = ["created_at", "title", "due_date"]
    search_fields = ["title", "description"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "color"]
    search_fields = ["name"]
