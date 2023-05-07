from django.contrib import admin

from pay.models import Pay, Payment, Charge, Order

admin.site.register(Pay)
admin.site.register(Payment)
admin.site.register(Charge)
admin.site.register(Order)
