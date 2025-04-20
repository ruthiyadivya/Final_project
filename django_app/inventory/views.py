from django.shortcuts import render, redirect
from .models import Item

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('description')
        if name and desc:
            Item.objects.create(name=name, description=desc)
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
