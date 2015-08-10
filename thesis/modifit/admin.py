from django.contrib import admin

# Register your models here.

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
	inlines = [hasSubCategoryInline, hasSizeInline, hasColorInline, hasPatternInline, hasMaterialInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Pattern)
admin.site.register(Material)