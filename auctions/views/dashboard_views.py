from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, TemplateView
from auctions.forms import UserProfileForm

from auctions.models import Comment, UserProfile

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
        # Fetch comments for each chart
        context['bar_chart_comments'] = Comment.objects.filter(chart_id='barChart')
        context['line_graph_comments'] = Comment.objects.filter(chart_id='lineGraph')
        context['pie_chart_comments'] = Comment.objects.filter(chart_id='pieChart')
        context['radar_chart_comments'] = Comment.objects.filter(chart_id='radarChart')
        context['polar_chart_comments'] = Comment.objects.filter(chart_id='polarAreaChart')
        context['doughnut_chart_comments'] = Comment.objects.filter(chart_id='doughnutChart')
        context['bubble_chart_comments'] = Comment.objects.filter(chart_id='bubbleChart')
        context['scatter_plot_comments'] = Comment.objects.filter(chart_id='scatterPlot')
        context['area_chart_comments'] = Comment.objects.filter(chart_id='areaChart')
        
        return context

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['profile_picture', 'bio']
    template_name = 'auctions/edit_profile.html'
    success_url = reverse_lazy('dashboard')


@login_required
def user_profile_view(request):
    user_profile = request.user
    user_comments = Comment.objects.filter(user=request.user)
    profile_pic = UserProfile.objects.get(user=request.user).profile_picture
    bio = UserProfile.objects.get(user=request.user).bio
    age = UserProfile.objects.get(user=request.user).age
    city = UserProfile.objects.get(user=request.user).city
    state = UserProfile.objects.get(user=request.user).state
    interests = UserProfile.objects.get(user=request.user).interests
    
    return render(request, 'auctions/profile.html', {
        'user_profile': user_profile,
        'user_comments': user_comments,
        'profile_pic': profile_pic,
        'bio': bio,
        'age': age,
        'city': city,
        'state': state,
        'interests': interests
    })

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