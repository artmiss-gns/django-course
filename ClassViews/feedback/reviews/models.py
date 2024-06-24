from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    rating = models.IntegerField()
    review = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.pk}:{self.name}-{self.last_name}"