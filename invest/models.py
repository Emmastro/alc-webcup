from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Investment(models.Model):
    """
    The investor can have multiple investments, each to different mining farms
    """
    mining_farm = models.ForeignKey('farm.MiningFarm', on_delete=models.CASCADE)
    amount = models.IntegerField()


class Investor(User):
    """
    Without authentication, users can see the list of mining farms available in the island and their profile.
    Upon registration as investor, the user can choose a mining farm, choose investment option and investor
    A user can invest in more than one mining farm
    """
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to="mining_farm/logo", null=True, blank=True)
    investment = models.ManyToManyField(Investment)

    def avatar_url(self):
        """
        User profile url
        """
        if self.avatar and hasattr(self.avatar, "url"):
            return self.avatar.url

    def get_absolute_url(self):
        return reverse('mining-farm', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        """Administrator full name"""
        return "{self.first_name} {self.last_name}"
