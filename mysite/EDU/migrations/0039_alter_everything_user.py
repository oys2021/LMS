# Generated by Django 4.0 on 2022-02-10 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('EDU', '0038_everything_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everything',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
