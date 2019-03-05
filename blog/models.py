from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100) #text
    content = models.TextField() #image
    date_posted = models.DateTimeField(default= timezone.now) #date
    author = models.ForeignKey(User, on_delete=models.CASCADE) #when user is deleted all posts are deleted as well

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})


