# Generated by Django 4.2.18 on 2025-01-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aeroplane',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
