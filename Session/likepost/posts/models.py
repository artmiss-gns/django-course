from django.db import models

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images', null=True) # MEDIA_ROOT/post_images