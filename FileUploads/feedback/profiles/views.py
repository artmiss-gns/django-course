from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FileUploadForm
from .models import UserImage

def save_file(file):
    file_postfix = file.__str__().partition('.')[-1]
    with open(f'tmp/image.{file_postfix}', 'wb+') as new_file :
        for chunk in file.chunks() :
            new_file.write(chunk)
            
class CreateProfileView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(
            request, "profiles/create_profile.html",
            context={'form': form}
        )
    
    def post(self, request):
        submitted_form = FileUploadForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            image = UserImage(image=submitted_form.cleaned_data['user_image'])
            image.save()
            return render(request, 'profiles/success_upload.html')
        else :
            return render(
                request, "profiles/create_profile.html",
                context={'form': submitted_form}
            )
