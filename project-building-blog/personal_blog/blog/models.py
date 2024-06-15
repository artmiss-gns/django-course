from django.db import models
from personal_blog.settings import BASE_DIR

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_add = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.first_name}  {self.last_name}"
    
class Tag(models.Model):
    name = models.CharField(max_length=16)
    
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=32)
    excerpt = models.CharField(max_length=64)
    image_add = models.FilePathField(path=BASE_DIR/'blog'/'static'/'blog'/'images',null=True)
    date = models.DateField(null=False)
    slug = models.SlugField()
    content = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, null=True)
    
    
    def __str__(self) -> str:
        return f"Post: {self.title}"