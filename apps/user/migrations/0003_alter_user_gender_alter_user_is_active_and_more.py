# Generated by Django 5.1.1 on 2024-10-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_phone_user_phone_number_user_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
