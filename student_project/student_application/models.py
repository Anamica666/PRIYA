# student_application/models.py

from django.db import models

class StudentInfo(models.Model):
    name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(blank=False)
    student_class = models.CharField(max_length=255, blank=False)
