# Generated by Django 5.0.1 on 2024-01-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pic',
            field=models.ImageField(default='gallery', upload_to=''),
        ),
    ]