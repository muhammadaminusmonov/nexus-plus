# Generated by Django 5.1.7 on 2025-03-12 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productreview_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.SmallIntegerField()),
                ('status', models.SmallIntegerField(choices=[(1, 'ACTIVE'), (2, 'INACTIVE')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
