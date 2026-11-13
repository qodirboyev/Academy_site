from django.db import models

# Create your models here.



class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_info = models.TextField()
    course_lesson = models.IntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.course_name



class Lessons(models.Model):
    lesson_number = models.IntegerField()
    lesson_subject = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson_number}-Dars. Mavzu:{self.lesson_subject}'




class Teachers(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_surname = models.CharField(max_length=100)
    teacher_photo = models.ImageField(upload_to='teachers_photo')
    teacher_skills = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_surname}"
