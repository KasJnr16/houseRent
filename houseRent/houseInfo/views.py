from django.shortcuts import render, get_object_or_404, redirect
from .forms import HouseForm
from .models import House
from core.views import profile

# Create your views here.


def viewHomeDetail(request, pk):
    house = get_object_or_404(House, pk=pk)
    related_houses = House.objects.filter(category=house.category, for_rent=True).exclude(pk=pk)[0:3]
    user = profile(request)

    return render(request, 'houseInfo/homeDetail.html',{
        'house': house,
        'related_houses': related_houses,
        'user': user,       
    })
    return

def uploadHome(request):
    user = profile(request)
    form = HouseForm()
    if request.method == "POST":
        form = HouseForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form = form.save(commit=False)
                form.created_by = request.user
                form.save()
        except Exception as e:
            print("Error in saving user to database", str(e))
    
    if request.method == "GET":
         form = HouseForm()

    return render(request, "houseinfo/formHome.html",{
        "form": form,
        "title":"Upload House Details",
        "user": user,
    })

def updateHome(request, pk):
    user = profile(request)
    house = get_object_or_404(House, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = HouseForm(request.POST, request.FILES, instance = house)
        if form.is_valid():
            form.save()

    else:
        form = HouseForm(instance=house)
    
    return render(request, "houseInfo/formHome.html",{
        "form": form,
        "title": f"Update {house}",
        "user": user,
    })

def deleteHome(request,pk):
    house = get_object_or_404(House, pk=pk, created_by=request.user)
    house.delete()

    pass

