# Generated by Django 5.0.6 on 2024-06-24 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_alter_componentpc_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentpc',
            name='brand',
        ),
    ]