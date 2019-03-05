# Generated by Django 2.1.7 on 2019-03-05 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends_fl', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='users_fl', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='friend',
            name='current_user',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
