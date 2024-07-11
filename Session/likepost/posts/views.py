from typing import Any
from django.shortcuts import render
# from django.views import View
from django.views.generic import View
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import PostModel
from .forms import PostForm
# Create your views here.

class Post(TemplateView):
    template_name = 'posts/post.html'
    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context['posts'] = PostModel.objects.all()
        return context

class AddPost(View):
    def get(self, request):
        form = PostForm()
        return render(
            request, 'posts/add_post.html', context={'form': form}
        )
        
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        print('#'*10)
        if form.is_valid() :
            # saving the data in database
            title, content, image = request.POST.get('title'), request.POST.get('content'), request.FILES.get('image')
            
            new_post = PostModel(title=title, content=content, image=image)
            new_post.save()
            messages.success(request, "Success!", extra_tags='alert alert-success')
            return HttpResponseRedirect(reverse('add-post'))
        else :
            print(form.errors)
            messages.success(request, "Fill the required fields" , extra_tags='alert alert-danger')
            return HttpResponseRedirect(reverse('add-post'))
    
class SuccessfulSubmit(TemplateView):
    template_name = 'posts/successful_submit.html'
    
class LikePost(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('post'))
    def post(self, request):
        if request.session.get('liked') :
            request.session['liked'] = False
        else :
            request.session['liked'] = True
        return render(
            request, 'posts/post.html', context={
                'posts': PostModel.objects.all(),
                'is_liked': request.session.get('liked')
            }
        )