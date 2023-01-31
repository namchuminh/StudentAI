from django.db import models
from datetime import datetime

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name
    
class ClassName(models.Model):
    name = models.CharField(max_length=255, null=False)
    number = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Students(models.Model):
    fullname = models.CharField(max_length=255, null=False)
    birthday = models.DateField(null=False)
    gender = models.BooleanField(null=False)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to ='students/', blank=True, null=True)
    phone = models.CharField(max_length=11)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    joining_date = models.DateField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.fullname + " - " + self.classname.name


    