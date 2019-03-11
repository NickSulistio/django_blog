from django.contrib import admin
from .models import Profile, Publication, Article

admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Profile)

# Register your models here.
