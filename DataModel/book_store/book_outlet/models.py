from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    author = models.CharField(max_length=128)
    is_bestseller = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    slug = models.SlugField(default='', null=False, db_index=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # FIXME: this can cause problems if 2 books have the same title and should be fixed later
        
    def get_absolute_url(self):
        return reverse("book_page", kwargs={"slug": self.slug}) # you could also use self.pk 
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.title})"