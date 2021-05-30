from django.shortcuts import render
from invest.models import Investor


def edit_details(request):
    # TODO: load a form to edit farm details
    # Details to edit: Descripion, 
    return render(request, "edit_details.html", context=locals())


def investors(request):
    farms = Investor.objects.all()
    return render(request, "investors.html", context=locals())
