# Generated by Django 4.0 on 2022-02-11 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0049_remove_everything_user_enroll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='everything',
        ),
        migrations.AddField(
            model_name='everything',
            name='enroll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EDU.enroll'),
        ),
    ]
