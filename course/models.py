from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=9)
    course_name = models.CharField(max_length=60)
    section = models.CharField(max_length=5, blank=True)
    credits = models.IntegerField()
    schedule = models.CharField(max_length=60, blank=True)
    classroom = models.CharField(max_length=10, blank=True)
    professor = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return (self.course_code + " - " + self.course_name)

class Event(models.Model):
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    date = models.DateField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Location(models.Model):
    building_code = models.CharField(max_length=10)
    building_name = models.CharField(max_length=60)
    embed = models.TextField()

    def __str__(self):
        return self.building_code + " - " + self.building_name