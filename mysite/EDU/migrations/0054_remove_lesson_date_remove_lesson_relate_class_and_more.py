# Generated by Django 4.0 on 2022-03-02 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0053_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='relate_class',
        ),
        migrations.AddField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EDU.everything'),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]