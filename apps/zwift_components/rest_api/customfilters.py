import django_filters
from django_filters import filters
from apps.zwift_components import models

class CharArrayFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass
class IntegerFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass
class FlotFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass

class FilterFilter(django_filters.FilterSet):
    time = CharArrayFilter()
    height = CharArrayFilter()
    avg_hr = CharArrayFilter()
    max_hr = CharArrayFilter()
    hrmax = CharArrayFilter()
    weight = CharArrayFilter()
    np = CharArrayFilter()
    hrr = CharArrayFilter()
    hreff = CharArrayFilter()
    avg_power = CharArrayFilter()
    avg_wkg = CharArrayFilter()
    wkg_ftp = CharArrayFilter()
    wftp = CharArrayFilter()
    wkg1200 = CharArrayFilter()
    wkg300 = CharArrayFilter()
    wkg120 = CharArrayFilter()
    wkg60 = CharArrayFilter()
    wkg30 = CharArrayFilter()
    wkg15 = CharArrayFilter()
    wkg5 = CharArrayFilter()
    w1200 = CharArrayFilter()
    w300 = CharArrayFilter()
    w120 = CharArrayFilter()
    w60 = CharArrayFilter()
    w30 = CharArrayFilter()
    w15 = CharArrayFilter()
    w5 = CharArrayFilter()
    info_notes = CharArrayFilter()
    class Meta:
        model = models.TeamResult
        fields = ['DT_RowId', 'ftp', 'friend', 'pt', 'label', 'zid',
                  'pos', 'position_in_cat', 'name', 'cp', 'zwid', 'res_id',
                  'lag', 'uid', 'time', 'time_gun', 'gap', 'vtta', 'vttat',
                  'male', 'tid', 'topen', 'tname', 'tc', 'tbc', 'ff', 'tbd',
                  'zeff', 'category', 'height', 'flag', 'avg_hr', 'max_hr',
                  'hrmax', 'hrm', 'weight', 'power_type', 'display_pos',
                  'src', 'age', 'zada', 'note', 'div', 'divw', 'skill',
                  'skill_b', 'skill_gain', 'np', 'hrr', 'hreff', 'avg_power',
                  'avg_wkg', 'wkg_ftp', 'wftp', 'wkg_guess', 'wkg1200', 'wkg300',
                  'wkg120', 'wkg60', 'wkg30', 'wkg15', 'wkg5', 'w1200', 'w300',
                  'w120', 'w60', 'w30', 'w15', 'w5', 'is_guess', 'upg', 'penalty',
                  'reg', 'fl', 'pts', 'pts_pos', 'info', 'info_notes', 'f_t', 'ed']
