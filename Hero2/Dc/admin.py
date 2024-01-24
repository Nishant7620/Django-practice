from django.contrib import admin
from Dc.models import batman
# Register your models here.
@admin.register(batman)
class DcAdmmin(admin.ModelAdmin):
    list_display = ['id','name','heroic_name']

# admin.site.register(batman)