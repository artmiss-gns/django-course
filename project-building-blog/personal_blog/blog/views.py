from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.

def main_page(request):
    # chosen_posts = sorted(data, key=lambda post: post['date'], reverse=True)[0:3]
    chosen_posts = Post.objects.order_by('-date')[:3]
    context = {
        'data': chosen_posts,
    }
    return render(request, 'blog/index.html', context=context)
    
    
def all_blogs(request):
    '''all the posts'''
    data = Post.objects.all()
    context = {
        'posts': data,
    }
    return render(
        request, 'blog/blogs.html', context=context,
    )


def single_blog(request, slug:str):
    post = Post.objects.get(slug=slug)
    context = {
        'post':post,
    }
    return render(
        request, 'blog/single_blog.html', context=context,
    )