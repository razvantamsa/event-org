# Generated by Django 3.2.7 on 2021-10-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
