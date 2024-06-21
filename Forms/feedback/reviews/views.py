from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm


def review(request):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'reviews/main.html', {'form': form})
        
    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thank_you')
        
def thank_you(request):
    return render(
        request, 'reviews/thank_you.html'
)