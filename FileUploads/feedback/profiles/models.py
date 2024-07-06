from django.db import models

class UserImage(models.Model):
    image = models.FileField(upload_to='images') # MEDIA_ROOT/images