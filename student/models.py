from django.db import models

# Create your models here.
class Student(models.Model):
    prenom=models.CharField(max_length=50)
    note=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.prenom} ({self.note})"