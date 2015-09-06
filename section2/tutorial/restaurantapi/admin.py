from django.contrib import admin
from tutorial.restaurantapi.models import Menu, MenuItem

# Register your models here.

class MenuAdmin(admin.ModelAdmin):

	list_display = ['id', 'name', 'description', 'chef', 'available']


class MenuItemAdmin(admin.ModelAdmin):

	list_display = ['id', 'name', 'description', 'cost_to_make',
		'sale_price', 'available', 'menu']

