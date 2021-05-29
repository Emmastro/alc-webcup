from django.shortcuts import render, redirect

from django.views.generic.edit import UpdateView, CreateView
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

# from .forms import *
from invest.models import *
from farm.models import *


def account_redirect(request):
    return redirect('accounts', request.user.id)


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
