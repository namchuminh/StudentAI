from django.db import models
from datetime import datetime
from django.utils.text import slugify 
from django.contrib.auth.models import User

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name
    
class ClassName(models.Model):
    name = models.CharField(max_length=255, null=False)
    number = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ClassName, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
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


    