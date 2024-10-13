from django.urls import path
from .models import Post
from .import views
from django.views.generic import ListView, DetailView
urlpatterns = [
    path('',ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = 'blogs/blogs.html',
        context_object_name = 'Posts',
        paginate_by = 10)
        , name='blogs'),

    path('<int:pk>/', views.post,name='post'),
]