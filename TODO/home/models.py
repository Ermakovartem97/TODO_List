from django.db import models

class Task(models.Model):
    NameTask = models.CharField(max_length=32, blank=False, default="")
    TaskText = models.TextField(max_length=32, blank=True, null=True, default="")
    is_active = models.BooleanField(default=None)

    def __str__(self):
        return self.NameTask
