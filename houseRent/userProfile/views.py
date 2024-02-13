from django.shortcuts import render, get_object_or_404
from .forms import ProfileInformationForm
from .models import ProfileInformation
from django.contrib.auth.models import User
# Create your views here.
def userProfile(request):
    currentUser = request.user
    user, created = ProfileInformation.objects.get_or_create(user=currentUser)
    form = ProfileInformationForm(instance=user)

    if request.method == "POST":
            form = ProfileInformationForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
            
    return render(request, 'userProfile/profile.html', {
        "user": user,
        "title": f"{request.user}'s Profile",
        "form": form
    })

