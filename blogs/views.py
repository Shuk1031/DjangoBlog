from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'blog_list'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('list')
    

class BlogDetailView(DetailView, CreateView):
    model = Blog
    form_class = CommentForm
    template_name = 'blog/detail.html'
    context_object_name = 'blog_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comments.all()
        context['comment_form'] = CommentForm()
        return context

    def form_valid(self, form):
        form.instance.blog = self.get_object()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog/detail', kwargs={'pk': self.get_object().pk})
class BlogUpdateView(UpdateView):
    model = Blog
    forms_class = BlogForm
    fields = ('text',)
    template_name = 'blog/update.html'
    def get_success_url(self):
        return reverse_lazy('blog/detail', kwargs={'pk' : self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    forms_class = BlogForm
    fields = ('text',)
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('list')


