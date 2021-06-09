from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    dept=models.IntegerField()

    def __str__(self):
        return self.firstname

# Create your models here.
