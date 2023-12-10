from django.contrib import admin

# Register your models here.
from .models import Inspection,Park

admin.site.register(Inspection)
admin.site.register(Park)