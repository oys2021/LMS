# Generated by Django 4.0 on 2022-02-10 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EDU', '0046_remove_everything_enrolled_delete_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='everything',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
    ]
