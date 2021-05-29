from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class InvestmentOption(models.Model):
    """
    """
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class MiningFarm(User):
    """
    The administrator of each mining farm can create an account for the whole organisation
    The account gives them access to the admin dashboard, with privilege for editing their profile and
    Managing people who signup for investing to their farm, the investment option and other relevant details
    """
    farm_name = models.CharField(null=True, max_length=128)
    description = models.TextField(null=True)
    logo = models.ImageField(upload_to="mining_farm/logo", null=True, blank=True)
    investment_options = models.ManyToManyField(InvestmentOption)

    def logo_url(self):
        if self.logo and hasattr(self.logo, "url"):
            return self.logo.url

    def get_absolute_url(self):
        return reverse('mining-farm', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        """Administrator full name"""
        return "{self.first_name} {self.last_name}"

