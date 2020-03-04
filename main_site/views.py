from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Announce


def home(request):
    context = {
        'title': 'Home',
        'announcements': Announce.objects.all(),
    }
    return render(request, 'main_site/index.html', context)

def about(request):
    return render(request, 'main_site/about.html', {'title': 'About'})

def blog(request):
    context = {
        'title': 'Blog',
        'posts': Post.objects.all(),
    }
    return render(request, 'main_site/blog.html', context)

def faq(request):
    return render(request, 'main_site/faq.html', {'title': 'FAQ'})

def release(request):
    return render(request, 'main_site/release.html', {'title': 'Release Notes'})

def calendar(request):
    return render(request, 'main_site/calendar.html', {'title': 'Calendar'})

def media(request):
    return render(request, 'main_site/media.html', {'title': 'Media'})

################################################## POST #################################################

class PostListView(ListView):
    model = Post
    template_name = 'main_site/blog.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'main_site/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

@method_decorator(staff_member_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

################################################## POST #################################################

########################################## ANNOUNCEMENT #################################################

class AnnounceListView(ListView):
    model = Announce
    template_name = 'main_site/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    ordering = ['-date_posted']
    paginate_by = 5

class UserAnnounceListView(ListView):
    model = Announce
    template_name = 'main_site/user_announcements.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Announce.objects.filter(author=user).order_by('-date_posted')


class AnnounceDetailView(DetailView):
    model = Announce

@method_decorator(staff_member_required, name='dispatch')
class AnnounceCreateView(LoginRequiredMixin, CreateView):
    model = Announce
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnounceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announce
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author:
            return True
        return False

class AnnounceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announce
    success_url = '/'
    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author:
            return True
        return False

########################################## ANNOUNCEMENT #################################################