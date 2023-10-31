from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    context = {}
    return render(request, 'codedare_app/index.html', context)

def list_posts_view(request):
    context = {}
    return render(request, 'codedare_app/posts.html', context)


class PostsListView(generic.ListView):
    model = Post
    template_name = 'codedare_app/posts.html'
    context_object_name = 'posts'


class PostsDetailView(generic.DetailView):
    model = Post
    template_name = 'codedare_app/detail.html'
    context_object_name = 'post'


class PostsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'codedare_app/new.html'
    success_url = '/posts'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsUpdateView(generic.UpdateView):
    model = Post
    template_name = 'codedare_app/edit.html'
    fields = ['title', 'content' ]
    success_url = '/posts'
    

class PostsDeleteView(generic.DeleteView):
    model = Post
    template_name = 'codedare_app/confirm_delete.html'
    success_url = '/posts'

