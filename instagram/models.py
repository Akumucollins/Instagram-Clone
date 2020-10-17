from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# class Image(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
#     profile_photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
#     caption = models.TextField(max_length=1000)
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     likes= models.IntegerField(default=0)
#     dislikes= models.IntegerField(default=0)

#     def __str__(self):
#         return self.profile_photo[:3]
