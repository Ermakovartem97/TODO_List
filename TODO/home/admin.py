from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ["NameTask", "TaskText", "is_active"]

    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)