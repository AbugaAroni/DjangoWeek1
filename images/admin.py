from django.contrib import admin
from .models import Locations,Categories,Images
# Register your models here.


admin.site.register(Images)
admin.site.register(Locations)
admin.site.register(Categories)
