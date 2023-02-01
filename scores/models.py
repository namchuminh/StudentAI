from django.db import models
from students.models import Students, ClassName, Specialization
from subjects.models import Subject
# Create your models here.

class Scores(models.Model):
    score1 = models.FloatField(default=0)
    score2 = models.FloatField(default=0)
    score3 = models.FloatField(default=0)
    
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE, blank=True, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.classname = self.student.classname
        self.specialization = self.student.specialization
        super(Scores, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.subject.name  + " - " + self.student.fullname