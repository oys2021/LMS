# Generated by Django 4.0 on 2022-02-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0021_remove_enrolled_courses_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='everything',
            name='user',
        ),
        migrations.AddField(
            model_name='everything',
            name='classcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
