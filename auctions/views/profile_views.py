from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from auctions.models import UserProfile, Comment

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_comments = Comment.objects.filter(user=self.request.user)
        chart_id = Comment.objects.get(user=self.request.user).chart_id
        timestamp = Comment.objects.get(user=self.request.user).timestamp
        context['user_profile'] = user_profile
        context['user_comments'] = user_comments
        context['chart_id'] = chart_id
        context['timestamp'] = timestamp
        return context