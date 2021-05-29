from django.shortcuts import render
from farm.models import MiningFarm
from invest.models import  Investment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def mining_farms(request):
    farms = MiningFarm.objects.all()
    return render(request, "mining_farms.html", context=locals())

@login_required
def invest(request, farm_id):
    # TODO: Create an investment with the farm with id farm_id
    invest = Investment()
    return render(request, "invest.html", context=locals())

@login_required
def investment(request):
    # TODO: Only display investment of the user logged in
    investments = Investment.objects.all()
    return render(request, "investment.html", context=locals())

