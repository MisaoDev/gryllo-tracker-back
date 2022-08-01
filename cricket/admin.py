from django.contrib import admin

from cricket.models import Accessory, Cricket, CricketEvent, CricketMolt, Terrarium

admin.site.register(Cricket)
admin.site.register(Terrarium)
admin.site.register(Accessory)
admin.site.register(CricketEvent)
admin.site.register(CricketMolt)
