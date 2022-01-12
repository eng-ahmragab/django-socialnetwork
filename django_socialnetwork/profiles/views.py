from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Profile
from .forms import ProfileModelForm
from feed.forms import CommentModelForm


# messages types:
# messages.success(), messages.warning(), messages.error(), messages.info(), messages.debug()









@login_required
def profile(request, slug):
    profile = Profile.objects.filter(slug=slug).first()
    profile_form = ProfileModelForm(instance=profile)
    comment_form = CommentModelForm()
    context = {
        'profile': profile,
        'profile_form': profile_form,
        'comment_form': comment_form,
    }
    return render(request, 'profiles/profile.html', context)




@login_required
def update_profile(request, pk):
    # update profile form
    if request.method == 'POST':
        profile = Profile.objects.get(pk=pk)
        profile_form = ProfileModelForm(
            request.POST,
            files=request.FILES,
            instance=profile
        )
        
        # authorization
        if not profile.user == request.user:
            messages.warning(request, 'Your are not allowed to perform this action!')
            return redirect('profiles:profile', slug=profile.slug)
        
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            #redirect to prevent double form sending
            return redirect('profiles:profile', slug=profile.slug)
        context = {
            'profile': profile,
            'form': profile_form,
        }
        return render(request, 'profiles/profile.html', context)






@login_required
def profile_search(request):
    profile_list = []
    query = request.GET.get('query')
    if query:
        # Q is used for advanced search 'contains, .. etc'
        profile_list = Profile.objects.filter(Q(user__username__icontains=query))
    
    context = {
        'profile_list': profile_list,
    }

    return render(request, 'profiles/profile_list.html', context)
