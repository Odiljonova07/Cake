# Generated by Django 5.1.7 on 2025-03-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='finalPrice',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cake',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
