from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from farm.models import MiningFarm


class MiningFarmLoginForm(AuthenticationForm):

    model = MiningFarm

    def __init__(self, *args, **kwargs):
        super(MiningFarmLoginForm, self).__init__(*args, **kwargs)


class MiningFarmResetPasswordForm(PasswordResetForm):

    model = MiningFarm

    def __init__(self, *args, **kwargs):
        super(MiningFarmResetPasswordForm, self).__init__(*args, **kwargs)


class MiningFarmRegistrationForm(UserCreationForm):

    model = MiningFarm
