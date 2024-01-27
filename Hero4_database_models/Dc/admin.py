from django.contrib import admin
from Dc.models import Dc

#Register your models here.
@admin.register(Dc)
class DcAdmin(admin.ModelAdmin):
    list_display = ['name','heroic_name','city']

# admin.site.register(Dc)