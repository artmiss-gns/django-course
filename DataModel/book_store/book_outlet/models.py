from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    author = models.CharField(max_length=128)
    is_bestseller = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.title})"
