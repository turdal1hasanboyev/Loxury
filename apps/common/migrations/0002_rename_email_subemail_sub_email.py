# Generated by Django 5.1.1 on 2024-10-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subemail',
            old_name='email',
            new_name='sub_email',
        ),
    ]
