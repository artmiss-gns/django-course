from typing import Any
from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import TemplateView

from .models import Post, Comment
from .forms import AddCommentForm
# Create your views here.

# TODO : Convert the methods to ClassViews
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
            comment = Comment(author=request.POST['author'], comment_content=request.POST['comment_content'], post=Post.objects.get(slug=slug))
            comment.save()
            # return 200 OK 
            return HttpResponse("Form Submitted!", status=200)
            
        else :
            return HttpResponse("Invalid Form", status=400)
        
class ReadLaterView(TemplateView):
    template_name = 'blog/read_later.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        request = self.request
        print("#"*10)
        print(request.session.get('saved_page'))
        print("#"*10)
        context['saved_page'] = self.request.session.get('saved_page')
        return context
    
class SaveForLaterView(View):
    def get(self, request) : 
        return HttpResponse("Not Allowed", status=405)
    
    def post(self, request, slug) :
        saved_page = 'blogs/' + slug
        if request.session.get('saved_page') is None : # first time saving a post
            request.session['saved_page'] = [saved_page]
            return HttpResponse("Saved", status=200)
        
        if saved_page not in request.session.get('saved_page') : # if the post is not already saved
            request.session['saved_page'].append(saved_page)
            print("#"*10)
            print("HERE HAPPEND")
            print("#"*10)
            print(request.session.get('saved_page'))
            return HttpResponse("Saved", status=200)
        else :
            return HttpResponse("Already Saved", status=400)