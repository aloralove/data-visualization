from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, TemplateView

from auctions.models import UserProfile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'auctions/user_profile.html'
    context_object_name = 'profile'

class DashboardView(TemplateView):
    template_name = 'auctions/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include additional context for the dashboard, such as user preferences
        return context

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['profile_picture', 'bio']
    template_name = 'auctions/edit_profile.html'
    success_url = reverse_lazy('dashboard')


@login_required
def user_profile_view(request):
    return render(request, 'auctions/profile.html', {'user': request.user})