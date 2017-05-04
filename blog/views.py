from django.shortcuts import render,get_object_or_404
from .models import Post,Category,HeadPhoto
from django import forms
# Create your views here.


 
def index(requestuest):
    post_list = Post.objects.all()
    return render(requestuest, 'blog/index.html', context={'post_list': post_list})

def detail(requestuest,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(requestuest,'blog/detail.html',context={'post': post})

def archives(requestuest, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(requestuest, 'blog/index.html', context={'post_list': post_list})

def category(requestuest, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(requestuest, 'blog/index.html', context={'post_list': post_list})


