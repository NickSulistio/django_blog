# Generated by Django 2.1.7 on 2019-03-07 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190307_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendlist',
            old_name='friends',
            new_name='users',
        ),
    ]
