import django_filters
from .models import car, spare, engine
from . import models

class spareFilter(django_filters.FilterSet):
    
    Code = django_filters.CharFilter(field_name="spare_code",lookup_expr='icontains',label="Code")
    # spare_brand = django_filters.CharFilter(field_name="Brand",lookup_expr='icontains')
    # spare_name = django_filters.CharFilter(field_name="Type",lookup_expr='icontains')
    class Meta:
        model: spare
        fields = [
            "spare_code",            
        ]

 