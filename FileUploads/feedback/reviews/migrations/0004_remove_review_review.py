# Generated by Django 4.1 on 2024-07-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
    ]
