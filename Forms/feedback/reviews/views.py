from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == "GET":
        return render(request, 'reviews/main.html')
    elif request.method == "POST":
        return HttpResponseRedirect('thank_you')
        
def thank_you(request):
    return render(
        request, 'reviews/thank_you.html'
    )