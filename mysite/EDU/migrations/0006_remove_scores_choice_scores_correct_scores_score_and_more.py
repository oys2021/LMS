# Generated by Django 4.0 on 2021-12-20 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('EDU', '0005_scores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scores',
            name='Choice',
        ),
        migrations.AddField(
            model_name='scores',
            name='correct',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scores',
            name='score',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scores',
            name='wrong',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scores',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]