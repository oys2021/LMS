# Generated by Django 4.0 on 2022-02-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('EDU', '0032_rename_enrolled_courses_enrolled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
