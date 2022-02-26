# Generated by Django 4.0.2 on 2022-02-26 19:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwift_components', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamresult',
            name='DT_RowId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='age',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='avg_power',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='avg_wkg',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='f_t',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='ff',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='fl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='flag',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='ftp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='hreff',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='hrm',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='hrr',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='penalty',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='position_in_cat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='pt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='pts',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='pts_pos',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='res_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='tbc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='tbd',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='tc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='tid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='tname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='topen',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='vtta',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w120',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w1200',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w15',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w30',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w300',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='w60',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wftp',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg120',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg1200',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg15',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg30',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg300',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg60',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='wkg_ftp',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='zid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]