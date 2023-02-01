from django.db import models
from user.models import InfoUser
from students.models import Specialization
from django.utils.text import slugify 

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255, null=False)
    credits = models.IntegerField()
    teaching = models.BooleanField(default=True)
    infouser = models.ForeignKey(InfoUser, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)
    
    def __str__(self):
        return  self.name + " | " + self.infouser.user.first_name + " " + self.infouser.user.last_name
