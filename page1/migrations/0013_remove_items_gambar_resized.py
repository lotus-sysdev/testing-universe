# Generated by Django 5.0.2 on 2024-02-20 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0012_items_gambar_resized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='gambar_resized',
        ),
    ]
