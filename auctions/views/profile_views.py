from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from auctions.forms import UserProfileForm

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the logged-in user to the template
        return context


