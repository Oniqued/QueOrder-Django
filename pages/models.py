from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Contact(models.Model):
    name = models.CharField(max_length=20)
    tel_num = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    content = models.TextField()
    # status = models.CharField(max_length=20)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content[:20]
