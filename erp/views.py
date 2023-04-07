import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pesonalassignment_01.settings")
django.setup()

from django.shortcuts import render, redirect
from erp.forms import ProductForm, InboundForm, OutboundForm
from django.contrib.auth.decorators import login_required
from erp.models import Product, Inbound, Outbound, Inventory
from django.db import transaction
from django.db.models import Sum
from django.contrib.auth import get_user_model
# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/inventory')
    else:
        return redirect('/log-in')

def inventory(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            for p in Product.objects.values():
                inbound = Inbound.objects.filter(code_id=p['id'])
                outbound = Outbound.objects.filter(code_id=p['id'])
                if len(list(inbound)) < 1:
                    pass
                else:
                    if len(list(outbound)) < 1:
                        total_in = Inbound.objects.filter(code_id=p['id']).aggregate(Sum('quantity'))
                        check = Inventory.objects.filter(code_id=p['id'])
                        if len(list(check)) == 1:
                            inventory_a = Inventory.objects.get(code_id=p['id'])
                            inventory_a.total_quantity = total_in['quantity__sum']
                            inventory_a.size = p['size']
                            inventory_a.save()
                        else:
                            inventory_b = Inventory()
                            inventory_b.code_id = p['id']
                            inventory_b.name = p['name']
                            inventory_b.price = p['price']
                            inventory_b.size = p['size']
                            inventory_b.total_quantity = total_in['quantity__sum']
                            inventory_b.save()

                    else:
                        total_out = Outbound.objects.filter(code_id=p['id']).aggregate(Sum('out_quantity'))
                        total_in = Inbound.objects.filter(code_id=p['id']).aggregate(Sum('quantity'))
                        check = Inventory.objects.filter(code_id=p['id'])
                        if len(list(check)) == 1:
                            inventory_a = Inventory.objects.get(code_id=p['id'])
                            inventory_a.total_quantity = total_in['quantity__sum'] - total_out['out_quantity__sum']
                            inventory_a.size = p['size']
                            inventory_a.save()
                        else:
                            inventory_b = Inventory()
                            inventory_b.code_id = p['id']
                            inventory_b.name = p['name']
                            inventory_b.price = p['price']
                            inventory_b.size = p['size']
                            inventory_b.total_quantity = total_in['quantity__sum'] - total_out['out_quantity__sum']
                            inventory_b.save()

            inventory_all = Inventory.objects.all()

            return render(request, 'erp/inventory.html', {'inventory': inventory_all})
        else:
            return redirect('/log-in')

@login_required
def product_create(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'erp/product_create.html', {'form': form})
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/inventory')
        else:
            return render(request, 'erp/product_create.html', {'form': form})

@login_required
def product_list(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        return render(request, 'erp/product_list.html', {'product_list':product_list})


@login_required
@transaction.atomic
def inbound_create(request):
    if request.method == 'GET':
        form = InboundForm()
        return render(request, 'erp/inbound_create.html', {'form': form})
    elif request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
        else:
            return redirect('/inbound-create')


@login_required
@transaction.atomic
def outbound_create(request):
    if request.method == 'GET':
        form = OutboundForm()
        return render(request, 'erp/outbound_create.html', {'form': form})
    elif request.method == 'POST':
        form = OutboundForm(request.POST)
        if form.is_valid():
            outbound_code = form.cleaned_data.get('code')
            outbound_quantity = form.cleaned_data.get('out_quantity')
            total_out = Outbound.objects.filter(code = outbound_code)
            total_in = Inbound.objects.filter(code = outbound_code).aggregate(Sum('quantity'))
            if len(list(total_out)) < 1:
                if outbound_quantity > total_in['quantity__sum']:
                    return redirect('/outbound-create')
                else:
                    form.save()
                    return redirect('/inventory')
            else:
                total_out_sum = total_out.aggregate(Sum('out_quantity'))
                if total_out_sum['out_quantity__sum'] + outbound_quantity > total_in['quantity__sum']:
                    return redirect('/outbound-create')
                else:
                    form.save()
                    return redirect('/inventory')
        else:
            return redirect('/outbound-create')




def delete_all(request):
    Product.objects.all().delete()
    Inventory.objects.all().delete()
    Inbound.objects.all().delete()
    Outbound.objects.all().delete()
    return redirect('/')