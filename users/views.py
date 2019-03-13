from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FriendListUpdateForm, FriendListRemoveForm
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib.auth.models import User


def friendsList(request):
    if request.user.is_authenticated:
        friendsList = request.user.profile.friendList.all()
    else:
        friendsList = None
    return {
        'friendsList': friendsList,
    }



def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}! You can log-in now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        pf_form = FriendListUpdateForm(request.POST, current_user = request.user)
        rf_form = FriendListRemoveForm(request.POST, current_user = request.user)
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
        if pf_form.is_valid():
            possibleFriends = pf_form.cleaned_data.get('possibleFriends')
            request.user.profile.friendList.add(possibleFriends)
            messages.success(request,f'You have added {possibleFriends} as a friend!')
            return redirect('profile')
        if rf_form.is_valid():
            removeFriend = rf_form.cleaned_data.get('removeFriend')
            request.user.profile.friendList.remove(removeFriend)
            messages.success(request,f'You have removed {removeFriend} as a friend.')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)    
        pf_form = FriendListUpdateForm(current_user=request.user)
        rf_form = FriendListRemoveForm(current_user=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pf_form': pf_form,
        'rf_form': rf_form,
    }
    return render(request, 'users/profile.html', context)

"""
@login_required
def friend_add
@login_required
def add_friend(request,pk):
    new_friend = User.objects.get(pk=pk)
    Friendlist.add_friend(request.user, new_friend) 

    context = {'new_friend': new_friend
    }

    return render(request, 'friend_list.html')
@login_required
def remove_friend(request, pk):
    new_friend = User.objects.get(pk=pk)
    FriendList.lose_friend(request.user, new_friend)
"""