# Generated by Django 5.1.3 on 2024-11-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True),
        ),
    ]
