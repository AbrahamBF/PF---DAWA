# Generated by Django 5.0.6 on 2024-06-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_componentpc_brand_alter_brand_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='price',
        ),
        migrations.AddField(
            model_name='brand',
            name='shop',
            field=models.IntegerField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]