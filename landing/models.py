from django.db import models

# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.email}'