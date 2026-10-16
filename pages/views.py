from django.shortcuts import render, redirect
from .models import Item
from django.db.models import Sum, Count

def home(request):
    return render(request, "pages/home.html")

def add_item(request):
    if request.method == 'POST':
        Item.objects.create(
            name=request.POST.get('name'),
            category=request.POST.get('category'),
            quantity=request.POST.get('quantity'),
            unit_price=request.POST.get('unit_price'),
            description=request.POST.get('description')
        )
        return redirect('inventory_list')
    return render(request, 'pages/add_item.html')

def inventory_list(request):
    items = Item.objects.all().order_by('name')
    return render(request, 'pages/inventory_list.html', {'items': items})

def stock_summary(request):
    total_items = Item.objects.aggregate(total=Count('id'))['total'] or 0
    total_quantity = Item.objects.aggregate(qty=Sum('quantity'))['qty'] or 0
    total_value = sum(item.total_value() for item in Item.objects.all())
    low_stock = Item.objects.filter(quantity__lte=5)
    return render(request, 'pages/stock_summary.html', {
        'total_items': total_items,
        'total_quantity': total_quantity,
        'total_value': total_value,
        'low_stock': low_stock
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        success = True
    return render(request, 'pages/contact.html', {'success': success})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('inventory_list')    