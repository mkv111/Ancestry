from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(relations)
admin.site.register(relation_desc)
admin.site.register(relation_hierarchy)