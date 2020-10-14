from django.contrib import admin
from .models import Locations,Categories,Blog_Images
# Register your models here.


admin.site.register(Blog_Images)
admin.site.register(Locations)
admin.site.register(Categories)
