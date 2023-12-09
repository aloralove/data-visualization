from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, TemplateView, CreateView

from auctions.models import Comment, UserProfile


class CommentView(ListView):
    model = Comment
    template_name = 'auctions/dashboard.html'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = UserProfile.objects.all()
        return context
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment']
    template_name = 'auctions/comment.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['comment']
    template_name = 'auctions/comment.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'auctions/comment_delete.html'
    success_url = reverse_lazy('dashboard')