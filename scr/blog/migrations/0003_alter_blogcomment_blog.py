# Generated by Django 5.1.7 on 2025-03-11 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_comment_blogcomment_blog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
    ]
