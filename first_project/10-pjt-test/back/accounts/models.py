from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender = models.CharField(max_length=1, choices=[('M', '남성'), ('F', '여성')])
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    introduction = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
    )

    def __str__(self):
      return f'{self.nickname} ({self.username})'