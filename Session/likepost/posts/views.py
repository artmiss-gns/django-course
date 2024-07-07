from django.shortcuts import render
# from django.views import View
from django.views.generic import View
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

class Post(View):
    def get(self, request):
        return render(
            request, 'posts/post.html'
        )
    
    def post(self, request):
        print("#"*10)
        print(request.POST)
        print("#"*10)
        return request.POST



class AddPost(View):
    def get(self, request):
        return render(
            request, 'posts/add_post.html'
        )
        
    def post(self, request):
        messages.success(request, "Success!", extra_tags='alert alert-success')
        # return HttpResponseRedirect(reverse('successful-submit'))
        return HttpResponseRedirect(reverse('add-post'))
    
    
class SuccessfulSubmit(TemplateView):
    template_name = 'posts/successful_submit.html'