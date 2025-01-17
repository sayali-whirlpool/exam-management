from django.db import models
from exam_management_app.models.student import Student
from .test import Test

class StudentTest(models.Model):
    id = models.AutoField(primary_key=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['student', 'test']