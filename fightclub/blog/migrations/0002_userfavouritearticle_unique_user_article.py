# Generated by Django 5.0.2 on 2024-02-15 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userfavouritearticle',
            constraint=models.UniqueConstraint(fields=('user', 'article'), name='unique_user_article'),
        ),
    ]
