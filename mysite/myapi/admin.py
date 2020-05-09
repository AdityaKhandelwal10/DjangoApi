from django.contrib import admin
from .models import User, Stores

admin.site.register(User)
# Register your models here.
admin.site.register(Stores)
