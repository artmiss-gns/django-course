from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .forms import ReviewForm
from .models import Review


        
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
            

class ThankYou(TemplateView):
    template_name='reviews/thank_you.html'