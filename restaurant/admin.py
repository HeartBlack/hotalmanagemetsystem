from django.contrib import admin
from .models import Customer,Room,Booked,Category,Kitchen_items,Bar_items,Order
# # Register your models here.
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Booked)
admin.site.register(Category)
admin.site.register(Kitchen_items)
admin.site.register(Bar_items)
admin.site.register(Order)



