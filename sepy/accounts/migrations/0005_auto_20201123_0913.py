# Generated by Django 3.1 on 2020-11-23 00:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201117_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='followed_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
