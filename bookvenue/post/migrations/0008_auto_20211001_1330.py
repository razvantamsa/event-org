# Generated by Django 3.2.7 on 2021-10-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='post',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
