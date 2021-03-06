# Generated by Django 4.0 on 2022-02-11 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('EDU', '0051_class_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='user',
        ),
        migrations.RemoveField(
            model_name='everything',
            name='enroll',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.AddField(
            model_name='enroll',
            name='everything',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EDU.everything'),
        ),
        migrations.AddField(
            model_name='enroll',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EDU.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
