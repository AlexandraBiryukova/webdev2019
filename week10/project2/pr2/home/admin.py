from django.contrib import admin

# Register your models here.
from .models import HomeObject,Info


admin.site.register(HomeObject)
admin.site.register(Info)
