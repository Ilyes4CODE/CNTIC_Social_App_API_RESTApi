# Generated by Django 4.2.6 on 2023-10-27 09:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="dislikers",
            field=models.ManyToManyField(
                blank=True, related_name="disliked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="likers",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
