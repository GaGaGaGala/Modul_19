from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Buyer)
admin.site.register(Game)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    #fields = [('name', 'age'), 'balance']
    search_fields = ('name',)
    list_filter = ('balance', 'age',)
    fieldsets = (
        ('info1', {
            'fields':
                ('name', 'age')
        }),
        ('info2', {
            'fields':
                ('balance',)
        }),
    )