from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class TeamResult(models.Model):
    DT_RowId = models.CharField(max_length=200, null=True, blank=True)
    ftp = models.CharField(max_length=200, null=True, blank=True)
    friend = models.IntegerField()
    pt = models.CharField(max_length=200, null=True, blank=True)
    label = models.CharField(max_length=200, null=True, blank=True)
    zid = models.CharField(max_length=200, null=True, blank=True)
    pos = models.IntegerField()
    position_in_cat = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    cp = models.IntegerField()
    zwid = models.IntegerField()
    res_id = models.CharField(max_length=200, null=True, blank=True)
    lag = models.IntegerField()
    uid = models.IntegerField()
    time = ArrayField(
        models.FloatField()
    )
    time_gun = models.FloatField()
    gap = models.FloatField()
    vtta = models.CharField(max_length=200, null=True, blank=True)
    vttat = models.FloatField()
    male = models.IntegerField()
    tid = models.CharField(max_length=200, null=True, blank=True)
    topen = models.CharField(max_length=200, null=True, blank=True)
    tname = models.CharField(max_length=200, null=True, blank=True)
    tc = models.CharField(max_length=200, null=True, blank=True)
    tbc = models.CharField(max_length=200, null=True, blank=True)
    ff = models.CharField(max_length=200, null=True, blank=True)
    tbd = models.CharField(max_length=200, null=True, blank=True)
    zeff = models.IntegerField()
    category = models.CharField(max_length=200, null=True, blank=True)
    height = ArrayField(
        models.IntegerField()
    )
    flag = models.CharField(max_length=200, null=True, blank=True)
    avg_hr = ArrayField(
        models.IntegerField()
    )
    max_hr = ArrayField(
        models.IntegerField()
    )
    hrmax = ArrayField(
        models.IntegerField()
    )
    hrm = models.CharField(max_length=200, null=True, blank=True)
    weight = ArrayField(
        models.FloatField()
    )
    power_type = models.IntegerField()
    display_pos = models.IntegerField()
    src = models.IntegerField()
    age = models.CharField(max_length=200, null=True, blank=True)
    zada = models.IntegerField()
    note = models.CharField(max_length=200, null=True, blank=True)
    div = models.IntegerField()
    divw = models.IntegerField()
    skill = models.CharField(max_length=200)
    skill_b = models.IntegerField()
    skill_gain = models.CharField(max_length=200)
    np = ArrayField(
        models.IntegerField()
    )
    hrr = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    hreff = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    avg_power = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    avg_wkg = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg_ftp = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wftp = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg_guess = models.IntegerField()
    wkg1200 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg300 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg120 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg60 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg30 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg15 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    wkg5 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w1200 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w300 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w120 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w60 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w30 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w15 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    w5 = ArrayField(
        models.CharField(max_length=200, null=True, blank=True)
    )
    is_guess = models.IntegerField()
    upg = models.IntegerField()
    penalty = models.CharField(max_length=200, null=True, blank=True)
    reg = models.IntegerField()
    fl = models.CharField(max_length=200, null=True, blank=True)
    pts = models.CharField(max_length=200, null=True, blank=True)
    pts_pos = models.CharField(max_length=200, null=True, blank=True)
    info = models.IntegerField()
    info_notes = ArrayField(
        models.CharField(max_length=100, null=True, blank=True),
        blank=True
    )
    f_t = models.CharField(max_length=200, null=True, blank=True)
    ed = models.BigIntegerField()
