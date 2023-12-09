
from django.shortcuts import render, redirect, get_object_or_404
from auctions.models import UserProfile

from django.views.generic import ListView


class IndexView(ListView):
    model = UserProfile
    template_name = 'auctions/index.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.all()
        return context