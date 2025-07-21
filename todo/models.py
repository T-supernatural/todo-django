# models.py
from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10, blank=True, null=True)  # e.g., red, blue

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def is_today(self):
        return self.due_date == timezone.now().date()

    def is_upcoming(self):
        return self.due_date > timezone.now().date()

    def is_previous(self):
        return self.due_date < timezone.now().date() and not self.is_completed

    def __str__(self):
        return self.title
