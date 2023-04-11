from django.db import models
from django.contrib.auth.models import User
from students.models import Students

# Create your models here.

class InfoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    phone = models.CharField(max_length=11)
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
    