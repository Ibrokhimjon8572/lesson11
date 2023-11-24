from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Media

def load(request):
    return HttpResponse('this is load page')

def contents(request):
    posts = Post.objects.all()
    for post in posts:
        if post.title == 'uzavto':
            return redirect('https://example.com')
    return render(request=request, template_name='contents.html', context={'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    images = Media.objects.filter(post=pk)
    return render(request=request, template_name='post.html', context={'images':images, 'post':post})

