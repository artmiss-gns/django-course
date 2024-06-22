from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     name = forms.CharField(max_length=24)
#     last_name = forms.CharField(max_length=32)
#     rating = forms.IntegerField(min_value=1, max_value=5, required=True)
#     review = forms.CharField(widget=forms.Textarea, required=False)  

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['owner_comment']]
        
        labels = {
            "name": "Your Name",
            "review": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }