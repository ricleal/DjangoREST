from django.contrib import admin
from .models import Menu, MenuItem


from django.contrib import admin
from tutorial.restaurantapi.models import Menu, MenuItem

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'name', 'description', 'chef', 'available']


class MenuItemAdmin(admin.ModelAdmin):
    #pass
    # Collumns to display in the admin interface when listing all entries
    list_display = ['id', 'name', 'description', 'cost_to_make',
                    'sale_price', 'available', 'menu']


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
