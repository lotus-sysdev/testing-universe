# Generated by Django 5.0.2 on 2024-02-13 08:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_alter_mymodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
