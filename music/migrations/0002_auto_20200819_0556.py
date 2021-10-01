# Generated by Django 3.1 on 2020-08-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name_plural': 'Music'},
        ),
        migrations.AlterField(
            model_name='music',
            name='bgrnd_vid',
            field=models.FileField(upload_to='bgrnd_video/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='main_file',
            field=models.FileField(upload_to='music/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='thumbnail_img',
            field=models.ImageField(upload_to='thumbnail/'),
        ),
    ]
