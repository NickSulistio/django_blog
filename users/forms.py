from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile #FriendList

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Profile
        fields = ['image']

class FriendListUpdateForm(forms.Form):
    possibleFriends = forms.ModelChoiceField(queryset=User.objects.none(), empty_label="Please select a user to add")

    def __init__(self, *args, **kwargs):
        # Get current_user from parameters
        current_user = kwargs.pop('current_user')

        # Call the original init
        super().__init__(*args, **kwargs)

        # Set the possible friends
        self.fields['possibleFriends'].queryset = User.objects.exclude(friends__user=current_user)

class FriendListRemoveForm(forms.Form):
    removeFriend = forms.ModelChoiceField(queryset= User.objects.none(), empty_label= ('Please select a user to remove'))
    def __init__(self, *args, **kwargs):
        # Get current_user from parameters
        current_user = kwargs.pop('current_user')

        # Call the original init
        super().__init__(*args, **kwargs)

        # Set the possible friends
        self.fields['removeFriend'].queryset = current_user.profile.friendList.all()
"""        
class FriendListForm(forms.ModelForm):
    class Meta:
        model = FriendList
        fields = ['users']
        
class AddFriendForm(forms.Form):
    class Meta:
        possibleFriends = forms.ChoiceField(choices = User.objects.exculde.profile.friendList())
"""