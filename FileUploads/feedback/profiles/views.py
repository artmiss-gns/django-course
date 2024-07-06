from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

def save_file(file):
    file_postfix = file.__str__().partition('.')[-1]
    with open(f'tmp/image.{file_postfix}', 'wb+') as new_file :
        for chunk in file.chunks() :
            new_file.write(chunk)
            
class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        save_file(request.FILES["profile_picture"])
        return render(request, 'profiles/success_upload.html')
