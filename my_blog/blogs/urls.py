from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:pk>', views.blog_detail, name='blog-detail'),
    # path('like/<int:pk>', views.product_like, name='product-like'),
    path('create-blog/', views.create_blog, name = "create-blog"),
    path('dashboard-blogs', views.dash_blogs, name = "dash_blogs"),
    path("update-blog/<int:pk>/", views.update_blog, name="update-blog"),
    path("delete-blog/<int:pk>/", views.delete_blog, name="delete-blog"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),



]