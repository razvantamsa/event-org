# Generated by Django 3.2.7 on 2021-10-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20211002_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='Bucharest', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(default='Romania', max_length=50),
            preserve_default=False,
        ),
    ]
