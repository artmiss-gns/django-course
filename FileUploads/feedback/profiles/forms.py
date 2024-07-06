from django import forms


class FileUploadForm(forms.Form):
    user_image = forms.ImageField()