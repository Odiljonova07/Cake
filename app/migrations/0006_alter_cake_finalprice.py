# Generated by Django 5.1.7 on 2025-03-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cake_finalprice_alter_cake_isdiscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='finalPrice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
