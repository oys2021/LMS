# Generated by Django 4.0 on 2021-12-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDU', '0006_remove_scores_choice_scores_correct_scores_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='correct',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scores',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scores',
            name='wrong',
            field=models.IntegerField(null=True),
        ),
    ]
