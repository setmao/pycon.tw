# Generated by Django 3.0.3 on 2020-06-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0046_auto_20200319_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='labels',
            field=models.CharField(blank=True, max_length=128, verbose_name='labels'),
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='labels',
            field=models.CharField(blank=True, max_length=128, verbose_name='labels'),
        ),
    ]