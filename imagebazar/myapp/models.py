from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    info = models.TextField()

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=30)
    info = models.TextField()
    upload_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    image = models.ImageField(upload_to='images')
    cat = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
