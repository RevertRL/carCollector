# Generated by Django 5.0.4 on 2024-04-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.CharField(default='https://i.imgur.com/A2EDuDT.png', max_length=100),
        ),
    ]