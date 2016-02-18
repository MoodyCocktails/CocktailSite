from django.shortcuts import render
def drinks_list(request):
    return render(request, 'drinks/drinks_list.html', {})
# Create your views here.
