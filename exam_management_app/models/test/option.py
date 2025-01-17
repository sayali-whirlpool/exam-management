from django.db import models
from .question import Question

class Option(models.Model):
    id = models.AutoField(primary_key=True)
    option_text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)