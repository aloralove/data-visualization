from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, TemplateView
from auctions.forms import UserProfileForm

from auctions.models import UserProfile

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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

@login_required
def edit_user_profile(request):
    # Ensure that the user has a userprofile
    userprofile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save()
            # Redirect to the profile page
            return redirect('profile')
    else:
        form = UserProfileForm(instance=userprofile)

    return render(request, 'auctions/edit_profile.html', {'form': form})

@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', pk=request.user.pk)
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'auctions/upload_profile_picture.html', {'form': form})