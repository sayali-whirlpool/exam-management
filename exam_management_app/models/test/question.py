from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'MCQ'),
        ('FIB', 'FIB'),
        ('SQL', 'SQL'),
    ]
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=128)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)

    class Meta:
        unique_together = ('question_text', 'question_type')