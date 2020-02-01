from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50, verbose_name = "Başlıq")
    completed = models.BooleanField(verbose_name = "Vəziyyət")

    def __str__(self):
        return self.title
