from django.db import models
from django.contrib.auth.models import  User


class Patient(models.Model):
    patients = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    age = models.CharField(default='',max_length=255)
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    retina_image = models.ImageField(upload_to='image',blank=True,null=True)
    grade = models.CharField(default='',max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
