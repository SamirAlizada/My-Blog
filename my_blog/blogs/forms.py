from django.forms import ModelForm
from .models import Blog, Category

class BlogForm(ModelForm):
  class Meta:
    model = Blog
    fields = "__all__"

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    fields = "__all__"