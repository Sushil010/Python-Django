# Generated by Django 4.2.18 on 2025-01-31 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0002_aeroplane_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pilots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('aeroplanes', models.ManyToManyField(related_name='pilots', to='firstapp.aeroplane')),
            ],
        ),
        migrations.CreateModel(
            name='Blackbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('black_id', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('damage_date', models.DateTimeField()),
                ('blackbox', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blackbox', to='firstapp.aeroplane')),
            ],
        ),
        migrations.CreateModel(
            name='Aero_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')], max_length=1)),
                ('comment', models.TextField()),
                ('time_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('aero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='firstapp.aeroplane')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
