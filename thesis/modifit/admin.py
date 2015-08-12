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

	def get_list_display(self, request):
		print "Hello!"
		print request
		q = self.get_queryset(request)
		print q
		print ""
		for i in q:
			if i.created_by == request.user:
				print i
		print ""
		q.filter(created_by=request.user)
		print q
		print self.get_queryset(request)

		list_display = ('thumbnail', 'item_name', 'created_by', 'created_on', 'published')

		return list_display


	"""def changelist_view(self, request, extra_context=None):
		# just in case you are having problems with carry over from previous
		# iterations of the view, always SET the self.list_display instead of adding
		# to it

		if Item.created_by == request.user.id or request.user.is_superuser:
			self.list_display = ['thumbnail'] + ['item_name'] + ['created_by'] + ['created_on'] + ['published']

		return super(ItemAdmin, self).changelist_view(request, extra_context)"""


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


	"""def get_readonly_fields(self, request, obj=None):
		if obj and not request.user.is_superuser: # editing an existing object
			return self.readonly_fields + ('created_by', 'created_on', 'edited_by', 'edited_on')
		elif obj and request.user.is_superuser:
			return self.readonly_fields + ('created_on', 'edited_on')
		return self.readonly_fields"""

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Pattern)
admin.site.register(Material)