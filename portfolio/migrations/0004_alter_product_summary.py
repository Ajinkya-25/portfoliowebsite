# Generated by Django 4.2.18 on 2025-02-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='hi there'),
        ),
    ]
