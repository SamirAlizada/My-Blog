from django.db import models
from members.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    blog_image = models.ImageField(upload_to = 'blog_image')
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="author")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self) -> str:
        return f"{self.title} - {self.description}"