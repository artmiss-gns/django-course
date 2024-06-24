from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView

from .forms import ReviewForm
from .models import Review


        
class review(FormView):
    form_class=ReviewForm
    template_name='reviews/main.html'
    success_url='thank_you'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
            

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
    
class SingleReview(DetailView):
	template_name = "reviews/single_review.html"
	model = Review