from django.db import models

# Create your models here.

from django.db import models

class Review(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    user_name = models.CharField(max_length=5)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


