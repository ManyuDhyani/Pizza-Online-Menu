import django_filters
from .models import Prizesize

class PizzaFilter(django_filters.FilterSet):
    class Meta:
        model = Prizesize
        fields = ['prize', 'size', 'category']
