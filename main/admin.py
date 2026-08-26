from django.contrib import admin
from main.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "is_completed", "created_at")
    list_editable = ("is_completed",)
    search_fields = ("title",)
    list_filter = ("is_completed",)