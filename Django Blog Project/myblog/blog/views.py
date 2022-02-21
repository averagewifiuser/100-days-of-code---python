from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import AddCommentForm
from django.contrib.auth.models import User
from django.contrib import messages



# def home(request):
#     context = {
#         'title': 'Django Blog',
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



# class PostDetailView(DetailView):
#     model = Post

def post_detail(request, pk):
    form = AddCommentForm()
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        #adding extra to forms
        form.instance.author = request.user
        form.instance.post = post


        if form.is_valid():
            #saving the comment into the db
            form.save()
            messages.success(request, f'Your comment has been posted!')
            return redirect('post-detail', pk=pk)

    
    context = {
        'form':form,
        'object': post,
        'comments': Comment.objects.filter(post=post).order_by('-date_posted')
    }
    return render(request, 'blog/post_detail.html', context)


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False