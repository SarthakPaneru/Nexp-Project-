from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.customer.username