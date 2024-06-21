from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=24)
    last_name = forms.CharField(max_length=32)
    rating = forms.IntegerField(min_value=1, max_value=5, required=True)
    review = forms.CharField(widget=forms.Textarea, required=False)  
