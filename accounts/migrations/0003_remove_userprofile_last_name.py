# Generated by Django 3.0.3 on 2021-03-04 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200216_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]