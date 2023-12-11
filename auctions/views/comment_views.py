from django.http import HttpResponseForbidden, HttpResponseRedirect
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
    fields = ['content']
    template_name = 'auctions/comment.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.chart_id = self.request.POST.get('chart_id') 
        return super().form_valid(form)
    
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'auctions/comment_edit.html'
    success_url = reverse_lazy('dashboard')
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user
    
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'auctions/comment_delete.html'
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseForbidden()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)