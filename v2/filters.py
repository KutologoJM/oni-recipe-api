import django_filters
from v2.models import RecipeONI


class RecipeONIFilter(django_filters.FilterSet):
    min_spoil_time = django_filters.NumberFilter(field_name='spoil_time', lookup_expr='gte')
    max_spoil_time = django_filters.NumberFilter(field_name='spoil_time', lookup_expr='lte')

    dlc = django_filters.CharFilter(lookup_expr='iexact')  # or 'icontains' for fuzzy match
    food_quality = django_filters.CharFilter(lookup_expr='icontains')  # JSONField filter (string match)
    source = django_filters.CharFilter(lookup_expr='icontains')  # optional filter by source

    ingredient = django_filters.CharFilter(field_name='ingredients__slug', lookup_expr='iexact')

    class Meta:
        model = RecipeONI
        fields = ['dlc', 'source']  # explicitly list filterable fields
