# Generated by Django 3.2.13 on 2023-12-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20231111_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]