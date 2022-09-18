from django.shortcuts import redirect, render
from .models import Blog, Category
from .forms import BlogForm
from django.db.models import Q

def index(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        search = request.POST.get("search")
        results = Blog.objects.filter(Q(title__icontains=search))

        context = {
        'results' : results
        }

        return render(request, 'blogs.html', context)

    context = {
        'blogs' : blogs,
        'categories' : categories

    }

    return render(request, 'blogs.html', context)

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog' : blog
    }

    return render(request, 'blog_detail.html', context)

def category_detail(request, pk):
    # product = Products.objects.get(pk=pk)
    # context = {
    #     'product' : product
    # }

    # return render(request, 'product_detail.html', context)

    category = Category.objects.get(pk=pk)
    blogs = Blog.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        'blogs' : blogs,
        'category' : category,
        'categories' : categories
    }
    return render(request, 'category.html', context)

# def blog_like(request, pk):
#     blog = get_object_or_404(Blog, id=request.Products.get('product.pk'))
#     blog.likes.add(request.user)

#     return HttpResponseRedirect(reverse('product-detail'), args=[str(pk)])

def create_blog(request):
  form = BlogForm()
  if request.method == "POST":
    form = BlogForm(request.POST, request.FILES)

    if form.is_valid():
        
        form.save()
        return redirect("dash_blogs")
  
  context = {
    'form' : form
  }

  return render(request, 'create_blog.html', context) 

def dash_blogs(request):
  blogs = Blog.objects.all()

  context = {
    "blogs" : blogs,
  }

  return render(request, "dash_blogs.html", context)

def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, "update_blog.html", context)

def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('index')

def dynamic_articles_view(request):
    search = Blog.objects.filter(product_name__contains='Terry')
    context = {
      'search' : search
    }
    return render(request, "blog_detail.html", context)

# def selected_product(request):
#     selected_product = Selected.objects.all()
#     context = {
#         "selected_product" : selected_product
#     }

#     return render(request, "selected_product.html", context)