from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

from .models import Post, Comment
from .forms import AddCommentForm
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
        'tags': post.tag.all(),
    }
    return render(
        request, 'blog/single_blog.html', context=context,
    )
    
    
class AddCommentView(View):
    def get(self, request, slug):
        # Not allowed 
        return HttpResponse("Not Allowed", status=405)
    
    def post(self, request, slug):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            # saving the model
            print('#'*10)
            print(slug)
            print('#'*10)
            comment = Comment(author=request.POST['author'], comment_content=request.POST['comment_content'], post=Post.objects.get(slug=slug))
            comment.save()
            # return 200 OK 
            return HttpResponse("Form Submitted!", status=200)
            
        else :
            return HttpResponse("Invalid Form", status=400)