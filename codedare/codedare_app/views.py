from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, PostFilterForm, CommentForm, CommentFilterForm
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

    def get_queryset(self):

        form = PostFilterForm(self.request.GET)
        queryset = Post.objects.all()
        if form.is_valid():
        
            title_filter = form.cleaned_data.get('title_filter')
            start_date_filter = form.cleaned_data.get('start_date_filter')
            end_date_filter = form.cleaned_data.get('end_date_filter')
        
            if title_filter:
                queryset = queryset.filter(title__regex=title_filter)
            if start_date_filter:
                queryset = queryset.filter(date__gte=start_date_filter, )
            if end_date_filter:
                queryset = queryset.filter(date__lte=end_date_filter)

        print(queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostFilterForm()
        return context


class PostsDetailView(generic.DetailView):
    model = Post
    template_name = 'codedare_app/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = CommentFilterForm()
        context['comments'] = Comment.objects.filter(origin_post=self.object).order_by('-date')
        if self.request.method == 'GET':
            comment_filter_form = CommentFilterForm(self.request.GET)
            if comment_filter_form.is_valid():
                start_date_filter = comment_filter_form.cleaned_data.get('start_date_filter')
                end_date_filter =comment_filter_form.cleaned_data.get('end_date_filter')

            if start_date_filter:
                context['comments'] = context['comments'].filter(date__gte=start_date_filter, )
            if end_date_filter:
                context['comments'] = context['comments'].filter(date__lte=end_date_filter)

        return context


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


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'codedare_app/comment.html'
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.origin_post_id = self.kwargs['pk']  
        form.instance.author = self.request.user  
        return super().form_valid(form)
    

