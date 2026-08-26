from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва задачі")
    is_completed = models.BooleanField(default=False, verbose_name="Виконано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return self.title