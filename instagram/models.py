from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Post(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, default=0)
    dislikes= models.IntegerField(default=0)

    def __str__(self):
        return self.image_name
