from django.db import models


# Create your models here
class SinhVien (models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    grade = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name