# Generated by Django 3.1.6 on 2021-02-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210217_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/users/%Y/%m/%d'),
        ),
    ]
