from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    subtitle = models.CharField(max_length=100,default='')
    writer = models.CharField(max_length=100,default='')
    book_id = models.IntegerField( default='')
    price = models.IntegerField(default='')
    content = models.TextField(default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
