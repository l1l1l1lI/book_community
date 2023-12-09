from django.contrib.auth.models import User
from django.db import models
# Create your models here.



class Book(models.Model):
    book_name = models.TextField(null = True)
    writer = models.TextField()
    number_of_pages = models.PositiveIntegerField()
    subject = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject