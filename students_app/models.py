from django.db import models
from courses_app.models import Courses
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    course = models.TextField()
    status = models.CharField(max_length=100,choices=(("no_reading","Bitruvchi"),("reading","o‘qiyapti")))

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ['surname']