from django.test import TestCase
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pesonalassignment_01.settings")
django.setup()
from erp.models import Product, Inbound, Outbound, Inventory
a = Inventory.objects.filter(code_id='1')
print(list(a))