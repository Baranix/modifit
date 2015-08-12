from django.contrib import admin

# Register your models here.

from django.utils import timezone

from django.contrib.auth.models import User

from .models import Item, hasSize, hasColor
from .models import Category, SubCategory, hasSubCategory
from .models import Pattern, hasPattern
from .models import Material, hasMaterial


class SubCategoryInline(admin.TabularInline):
	model = SubCategory
	extra = 1
	verbose_name = "Subcategory"
	verbose_name_plural = "Subcategories"

class CategoryAdmin(admin.ModelAdmin):
	inlines = [SubCategoryInline]

class hasSubCategoryInline(admin.TabularInline):
	model = hasSubCategory
	extra = 1
	verbose_name = "Subcategory"
	verbose_name_plural = "Subcategories"

class hasPatternInline(admin.TabularInline):
	model = hasPattern
	extra = 1
	verbose_name = "Pattern"
	verbose_name_plural = "Patterns"

class hasMaterialInline(admin.TabularInline):
	model = hasMaterial
	extra = 1
	verbose_name = "Material"
	verbose_name_plural = "Materials"

class hasSizeInline(admin.TabularInline):
	model = hasSize
	extra = 1
	verbose_name = "Size"
	verbose_name_plural = "Sizes"

class hasColorInline(admin.TabularInline):
	model = hasColor
	extra = 1
	verbose_name = "Color"
	verbose_name_plural = "Colors"

class ItemAdmin(admin.ModelAdmin):
	inlines = [
		hasSubCategoryInline,
		hasSizeInline,
		hasColorInline,
		hasPatternInline, 
		hasMaterialInline
	]

	fieldsets = [
		(None, {'fields': ['item_name', 'published']}),
	]
	
	list_display = ('thumbnail', 'item_name', 'created_by', 'created_on', 'published')


	def thumbnail(self, obj):
		color = hasColor.objects.filter(item_id=obj.id)
		all_thumbs = ''
		for i in range(color.count()):
			all_thumbs = all_thumbs + '<img src="' + color[i].image.url + '" style="height:85px; width:auto;" />'
		return all_thumbs
	thumbnail.allow_tags = True


	def save_model(self, request, obj, form, change):
		if change:
			obj.edited_by = request.user
			obj.edited_on = timezone.now()
		else:
			obj.created_by = request.user
			obj.created_on = timezone.now()
		obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Pattern)
admin.site.register(Material)