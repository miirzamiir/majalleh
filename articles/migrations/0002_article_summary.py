# Generated by Django 3.1.6 on 2021-02-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
