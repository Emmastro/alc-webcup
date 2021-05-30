from django.shortcuts import render, redirect

from django.views.generic.edit import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# from .forms import *
from invest.models import *
from farm.models import *


def account_redirect(request):
    return redirect('accounts', request.user.id)



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'contact_number'): # investor
                return redirect('investors')
            else: # isinstance(user, MiningFarm):
                return redirect('mining_farms')

    return render(request, "login.html")


def register_investor(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        bio = request.POST['bio']

        investor = Investor(first_name=first_name, last_name=last_name, bio=bio, username=username)

        investor.set_password(password)
        investor.save()
        return redirect('mining_farms')
    
    else:
        return render(request, "registration_investor.html")

def register_farm(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        farm_name = request.POST['farm-name']
        description = request.POST['description']

        farm = MiningFarm(first_name=first_name, last_name=last_name, description=description, farm_name=farm_name, username=username)

        farm.set_password(password)
        farm.save()
        login(request, farm)
        return redirect('investors')

    else:
        return render(request, "registration_farm.html")

@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    """Update the user's details"""

    template_name = "account.html"
    # Model and form class depend on if the user is an investor or farm admin
    # model
    # form_class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: dynamically load the menu
        # context['lst_menu'] = # dynamically set the menu here

        return context
