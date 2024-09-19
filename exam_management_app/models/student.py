from django.db import models
from exam_management_app.models import College, Branch,Stream

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=100,choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone_no = models.CharField(max_length=10)
    college = models.ForeignKey(College, on_delete=models.CASCADE,null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True, blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE,null=True, blank=True)
