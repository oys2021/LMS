# Generated by Django 4.0 on 2022-03-08 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0054_remove_lesson_date_remove_lesson_relate_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='name',
        ),
    ]
