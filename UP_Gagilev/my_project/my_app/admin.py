from django.contrib import admin
from .models import Motosalon, MotorTransport, Dealer, Client, Accessory, Service, Deal, DealMotorTransport, DealService, DealAccessory  

admin.site.register(Motosalon)
admin.site.register(MotorTransport)
admin.site.register(Dealer)
admin.site.register(Client)
admin.site.register(Accessory)
admin.site.register(Service)
admin.site.register(Deal)
admin.site.register(DealMotorTransport)
admin.site.register(DealService)
admin.site.register(DealAccessory)