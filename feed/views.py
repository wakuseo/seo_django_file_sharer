from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostForm
from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post

class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('feed:index')  # Use reverse_lazy for success_url

    def form_valid(self, form):
        new_object = Post.objects.create(
            text=form.cleaned_data['text'], 
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was successful!")
        return super().form_valid(form)  # Use form_valid instead of form_invalid
