from django.contrib import admin
from .models import Editor,Locations,Categories,Images
# Register your models here.


admin.site.register(Editor)
admin.site.register(Images)
admin.site.register(Locations)
admin.site.register(Categories)
