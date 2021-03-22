# Generated by Django 3.0.3 on 2021-03-19 09:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20170429_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
