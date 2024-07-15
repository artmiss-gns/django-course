from django.db import models
from django.urls import reverse

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
    image = models.ImageField(upload_to="posts", null=True) # /media/posts/image.png
    date = models.DateField(null=False)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField(Tag, blank=True)
    
    
    def get_absolute_url(self):
        return reverse("single_blog", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return f"Post: {self.title}"


class Comment(models.Model):
    author = models.CharField(max_length=32)
    comment_content = models.TextField(null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self) -> str:
        return f"Comment(): {self.author}"