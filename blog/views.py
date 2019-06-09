from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    print(detail_blog.title)
    return render(request, 'blog/detail.html', {'blog':detail_blog})

# Create your views here.
