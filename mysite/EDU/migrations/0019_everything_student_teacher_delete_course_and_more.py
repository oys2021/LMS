# Generated by Django 4.0 on 2022-02-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0018_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Everything',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('coursecode', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Dates',
        ),
        migrations.RemoveField(
            model_name='question',
            name='relate_class',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.RemoveField(
            model_name='scores',
            name='user',
        ),
        migrations.DeleteModel(
            name='Update',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
    ]
