from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from houseInfo.models import House
from django.db.models import Q
from userProfile.models import ProfileInformation
from django.contrib.auth.models import User
# Create your views here.

def profile(request):
    currentUser = request.user
    user, created = ProfileInformation.objects.get_or_create(user=currentUser)
    
    if request.user:
        return user

def signUp(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")

    return render(request, "core/signUp.html",{
        "form":form,
    })

def welcome(request):
    return render(request,"core/welcome.html",{

    })

@login_required
def map(request):
    user = profile(request)
    return render(request,"core/map.html",{
        "user": user,
    })

@login_required
def index(request):
    user = profile(request)
    search = request.GET.get("search", "")
    house = House.objects.filter(for_rent=True)

    if search:
        house = house.filter(Q(house_name__icontains=search) | Q(description__icontains=search))
        
    return render(request,"core/index.html",{
        "house": house,
        "search": search,
        "user": user

    })



