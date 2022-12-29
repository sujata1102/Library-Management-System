from django.db import models
from datetime import datetime
# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    isbn=models.IntegerField()
    desc=models.CharField(max_length=500)
    is_deleted=models.CharField(max_length=5)
    upload=models.FileField()
    book_link=models.CharField(max_length=200)
    dt=models.DateTimeField(default=datetime.now)
    uid=models.IntegerField()
    uname=models.CharField(max_length=50)

    def __str__(self):
        return self.bname