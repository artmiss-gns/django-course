from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

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
    
    
class ListReviews(ListView):
    template_name='reviews/review_list.html'
    model=Review
    context_object_name='reviews'
    def get_queryset(self):
        query = super().get_queryset()
        query.filter(rating=4)
        return query
    