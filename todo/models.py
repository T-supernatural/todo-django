from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title