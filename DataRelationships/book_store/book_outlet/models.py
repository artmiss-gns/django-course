from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Address(models.Model):
    street = models.CharField(max_length=128)
    postal_code = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(10)])
    city = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return f"{self.city}:  {self.street}"
    
    class Meta:
        verbose_name_plural = 'Addresses'
        
class Author(models.Model):
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
            return f"{self.FirstName}:  {self.LastName}"
class Country(models.Model):
    name = models.CharField(max_length=128)
    code = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        verbose_name_plural = 'Countries'

class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestseller = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    countries_published = models.ManyToManyField(Country)
    slug = models.SlugField(default='', null=False, db_index=True)
        
    def get_absolute_url(self):
        return reverse("book_page", kwargs={"slug": self.slug}) # you could also use self.pk 
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.title})"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.title})"