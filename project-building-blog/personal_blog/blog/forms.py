from django import forms

class AddCommentForm(forms.Form):
    author = forms.CharField(max_length=24)
    comment_content = forms.CharField(widget=forms.Textarea, required=True)