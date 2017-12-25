from django.contrib import admin
from .models import Comments,userProfile

# Register your models here.
admin.site.register(Comments)
admin.site.register(userProfile)