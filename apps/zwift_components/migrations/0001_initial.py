# Generated by Django 4.0.2 on 2022-02-26 19:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DT_RowId', models.CharField(max_length=200)),
                ('ftp', models.CharField(max_length=200)),
                ('friend', models.IntegerField()),
                ('pt', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
                ('zid', models.CharField(max_length=200)),
                ('pos', models.IntegerField()),
                ('position_in_cat', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cp', models.IntegerField()),
                ('zwid', models.IntegerField()),
                ('res_id', models.CharField(max_length=200)),
                ('lag', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('time', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('time_gun', models.FloatField()),
                ('gap', models.FloatField()),
                ('vtta', models.CharField(max_length=200)),
                ('vttat', models.IntegerField()),
                ('male', models.IntegerField()),
                ('tid', models.CharField(max_length=200)),
                ('topen', models.CharField(max_length=200)),
                ('tname', models.CharField(max_length=200)),
                ('tc', models.CharField(max_length=200)),
                ('tbc', models.CharField(max_length=200)),
                ('ff', models.CharField(max_length=200)),
                ('tbd', models.CharField(max_length=200)),
                ('zeff', models.IntegerField()),
                ('category', models.CharField(max_length=200)),
                ('height', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('flag', models.CharField(max_length=200)),
                ('avg_hr', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('max_hr', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('hrmax', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('hrm', models.CharField(max_length=200)),
                ('weight', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('power_type', models.IntegerField()),
                ('display_pos', models.IntegerField()),
                ('src', models.IntegerField()),
                ('age', models.CharField(max_length=200)),
                ('zada', models.IntegerField()),
                ('note', models.CharField(max_length=200)),
                ('div', models.IntegerField()),
                ('divw', models.IntegerField()),
                ('skill', models.IntegerField()),
                ('skill_b', models.IntegerField()),
                ('skill_gain', models.IntegerField()),
                ('np', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('hrr', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('hreff', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('avg_power', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('avg_wkg', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg_ftp', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wftp', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg_guess', models.IntegerField()),
                ('wkg1200', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg300', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg120', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg60', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg30', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg15', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('wkg5', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w1200', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w300', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w120', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w60', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w30', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w15', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('w5', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('is_guess', models.IntegerField()),
                ('upg', models.IntegerField()),
                ('penalty', models.CharField(max_length=200)),
                ('reg', models.IntegerField()),
                ('fl', models.CharField(max_length=200)),
                ('pts', models.CharField(max_length=200)),
                ('pts_pos', models.CharField(max_length=200)),
                ('info', models.IntegerField()),
                ('info_notes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('f_t', models.CharField(max_length=200)),
                ('ed', models.BigIntegerField()),
            ],
        ),
    ]
