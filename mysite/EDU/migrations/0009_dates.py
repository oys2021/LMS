# Generated by Django 4.0 on 2021-12-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0008_rename_option1_questions_a_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
            ],
        ),
    ]
