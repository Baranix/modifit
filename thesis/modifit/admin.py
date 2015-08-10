from django.contrib import admin

# Register your models here.

from .models import Item, hasSize

class hasSizeInline(admin.TabularInline):
	model = hasSize
	extra = 1

class hasColorInline(admin.TabularInline):
	model = hasColor
	extra = 1

class ItemAdmin(admin.ModelAdmin):
	inlines = [hasSizeInline, hasColorInline]

admin.site.register(Item, ItemAdmin)