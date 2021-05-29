from django.shortcuts import render
from farm.models import MiningFarm

# Create your views here.
def home(request):
    farms = MiningFarm.objects.all()
    return render(request, "home.html", context=locals())
