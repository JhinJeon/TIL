from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=20)
    user = models.CharField(max_length=10)
    completed = models.BooleanField()

    def __str__(self):
        return self.title
