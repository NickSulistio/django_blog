from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics') 

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height> 300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class FriendList(models.Model):
    users = models.ManyToManyField(User)
    current_user =models.OneToOneField(User, related_name='friends', null=True, on_delete=models.CASCADE)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)
    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
    def __str__(self):
        return str(self.current_user)
"""
user1 = User.objects.create()
friendsList1 = FriendList.objects.create(current_user=user1)

user2 = User.objects.create()
friendsList1.users.add(user2) # Add user2 as friend of user1

print(user1.friends.all()) # print [user2]
print(friendsList1.current_user) # print user1
"""