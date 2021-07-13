from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    ContactNo= models.PositiveBigIntegerField()
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.name