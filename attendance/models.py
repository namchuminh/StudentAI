from pydoc import classname
from datetime import datetime
from django.db import models
from students.models import Students, ClassName
from subjects.models import Subject

# Create your models here.
class AttendanceInfo(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.classname.name + " - " +  self.subject.name + " - " + str(self.date)