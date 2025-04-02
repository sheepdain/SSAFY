from django.db import models

# Create your models here.
class  Diaries(models.Model):
    created_at=models.DateTimeField(auto_now=True)
    memo=models.TextField()