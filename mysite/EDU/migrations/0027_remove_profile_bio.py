# Generated by Django 4.0 on 2022-02-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0026_enrolled_courses_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Bio',
        ),
    ]