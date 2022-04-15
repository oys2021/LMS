# Generated by Django 4.0 on 2022-02-09 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('EDU', '0034_everything_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='everything',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
