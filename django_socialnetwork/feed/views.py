from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Post, Comment
from.forms import PostModelForm, CommentModelForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin





@login_required
def feed(request):
    post_form = PostModelForm()
    comment_form = CommentModelForm()
    posts = Post.objects.all()
    template_name = 'feed/feed.html' #needed for comment_form
    
    context = {
        'posts': posts,
        'post_form': post_form,
        'comment_form': comment_form,
        'template_name': template_name,
    }

    return render(request, template_name, context)


# set login_url in settings.py
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, files=request.FILES)
        comment_form = CommentModelForm()
        posts = Post.objects.all()
        success_url = 'feed:feed'
        template_name = 'feed/feed.html'
        if post_form.is_valid():
            author = request.user
            post = post_form.save(commit=False)
            post.author = author
            post.save()
            #redirect to prevent double form sending
            return redirect(success_url)

        context = {
            'query_set': posts,
            'post_form': post_form,
            'comment_form': comment_form,
        }
        return render(request, template_name, context)


@login_required
def add_comment(request):
    if request.method == 'POST':
        comment_form = CommentModelForm(request.POST)
        posts = Post.objects.all()
        post_form = PostModelForm()
        success_url = request.POST.get('success_url')
        template_name = request.POST.get('template_name')
        if comment_form.is_valid():
            author = request.user
            post_id = request.POST.get('post_id')
            post = Post.objects.get(pk=post_id)
            comment = comment_form.save(commit=False)
            comment.author = author
            comment.post = post
            comment.save()
            #redirect to prevent double form sending
            return redirect(success_url)
        else:
            context = {
                'query_set': posts,
                'post_form': post_form,
                'comment_form': comment_form,
            }
            return render(request, template_name, context)




@login_required
def like_unlike_post(request):
    if request.method == 'POST':
        success_url = request.POST.get('success_url')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        user = request.user
        # List of likes on the post
        likes_list = post.get_likes()
        # LIKE
        if user not in likes_list:
            post.likes.add(user)
        # UNLIKE
        else:
            post.likes.remove(user)
        #save changes
        post.save()
        return redirect(success_url)








class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'feed/post-delete.html'
    
    def get_queryset(self):
        pk = self.request.GET.get('pk')
        success_url = self.request.GET.get('success_url')
        self.kwargs['pk'] = pk
        self.success_url = success_url
        queryset = super(PostDeleteView, self).get_queryset()
        return queryset
    
    def get_success_url(self):
        return self.success_url
    
    #test if the logged in user if the post author
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user





class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'feed/post-update.html'
    
    def get_queryset(self):
        pk = self.request.GET.get('pk')
        success_url = self.request.GET.get('success_url')
        self.kwargs['pk'] = pk
        self.success_url = success_url
        queryset = super(PostUpdateView, self).get_queryset()
        return queryset
    
    def get_success_url(self):
        return self.success_url
    
    #test if the logged in user if the post author
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user