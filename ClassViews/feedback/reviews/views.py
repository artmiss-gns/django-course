from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm
from .models import Review

# def review(request):
#     if request.method == "GET":
#         form = ReviewForm()
#         return render(request, 'reviews/main.html', {'form': form})
        
#     elif request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('thank_you')
        
class review(View):
    def get(self, request):
        form = ReviewForm()
        return render(
            request, 'reviews/main.html', {'form': form}
        )
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank_you')
            

def thank_you(request):
    return render(
        request, 'reviews/thank_you.html'
)