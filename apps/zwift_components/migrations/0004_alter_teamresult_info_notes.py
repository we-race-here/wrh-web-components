# Generated by Django 4.0.2 on 2022-02-26 19:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwift_components', '0003_alter_teamresult_info_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamresult',
            name='info_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), blank=True, size=None),
        ),
    ]