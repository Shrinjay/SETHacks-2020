# Generated by Django 3.0.8 on 2020-07-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20200718_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='user',
            field=models.CharField(default='null', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobposting',
            name='user',
            field=models.CharField(default='null', max_length=120),
            preserve_default=False,
        ),
    ]
