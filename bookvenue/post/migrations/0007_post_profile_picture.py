# Generated by Django 3.2.7 on 2021-10-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]