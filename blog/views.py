from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.all().order_by('-date_posted')  # Get all blog posts
    return render(request, 'blog/index.html', {'blogs': blogs})
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})