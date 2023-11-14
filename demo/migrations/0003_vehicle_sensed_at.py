# Generated by Django 4.2.7 on 2023-11-13 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_vehicle_tolltransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='sensed_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
