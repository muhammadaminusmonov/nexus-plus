# Generated by Django 5.1.7 on 2025-04-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
