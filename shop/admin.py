from django.contrib import admin
from .models import Product,checkout,Contact,order,orderupdate
admin.site.register(Product)
admin.site.register(checkout)
admin.site.register(Contact)
admin.site.register(order)
admin.site.register(orderupdate)
# Register your models here.
