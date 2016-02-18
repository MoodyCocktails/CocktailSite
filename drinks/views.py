from django.shortcuts import render
from django.utils import timezone
from .models import Drink

def drinks_list(request):
    drinks = Drink.objects.order_by('name')
    return render(request, 'drinks/drinks_list.html', {'drinks':drinks})
