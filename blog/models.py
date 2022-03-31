from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to="image", null=True)
    date = models.DateField()
    excerpt = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True,related_name="posts")
    tag = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now=True , null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

