# Generated by Django 3.1 on 2020-08-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='categories',
            field=models.ManyToManyField(to='music.Category'),
        ),
    ]
