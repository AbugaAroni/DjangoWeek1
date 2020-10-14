from django.contrib import admin
from .models import Locations,Categories,Blog_Images
# Register your models here.

class Blog_ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Blog_Images, Blog_ImagesAdmin)
admin.site.register(Locations)
admin.site.register(Categories)
