# Generated by Django 3.0.3 on 2021-03-04 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='full_name',
        ),
    ]