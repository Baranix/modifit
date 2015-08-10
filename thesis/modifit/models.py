from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class UserAvatar(models.Model):
	user = models.ForeignKey(User)
	shoulder = models.DecimalField(max_digits=4, decimal_places=1, default=15, null=True, blank=True)
	bust = models.DecimalField(max_digits=4, decimal_places=1, default=34, null=True, blank=True)
	waist = models.DecimalField(max_digits=4, decimal_places=1, default=24, null=True, blank=True)
	hips = models.DecimalField(max_digits=4, decimal_places=1, default=34, null=True, blank=True)
	#length = models.PositiveIntegerField(default=0)
	height = models.DecimalField(max_digits=4, decimal_places=1, default=68, null=True, blank=True)

	SKINTONE_CHOICES = (
		('W', "Warm"),
		('C', "Cool"),
		('O', "Olive"),
		('N', "Neutral"),
	)
	skintone = models.CharField(max_length=1, choices=SKINTONE_CHOICES)


class Item(models.Model):
	item_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.item_name

class hasSize(models.Model):
	item = models.ForeignKey(Item)
	SIZE_CHOICES = (
		("XXS", "Extra, Extra Small"),
		("XS", "Extra Small"),
		("S", "Small"),
		("M", "Medium"),
		("L", "Large"),
		("XL", "Extra Large"),
		("XXL", "Extra, Extra Large"),
		("One", "One Size Fits All"),
	)
	size = models.CharField(max_length=3, choices=SIZE_CHOICES)
	shoulder = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	bust = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	waist = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	hips = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	length = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)

class hasColor(models.Model):
	item = models.ForeignKey(Item)
	red = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	green = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	blue = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])

class Patterns(models.Model):
	pattern_name = models.CharField(max_length=100, unique=True)

class hasPattern(models.Model):
	item = models.ForeignKey(Item)
	pattern = models.ForeignKey(Patterns)

class Materials(models.Model):
	material_name = models.CharField(max_length=100,unique=True)

class hasMaterials(models.Model):
	item = models.ForeignKey(Item)
	material = models.ForeignKey(Materials)

class Categories(models.Model):
	category_name = models.CharField(max_length=150, unique=True)

class hasCategory(models.Model):
	item = models.ForeignKey(Item)
	category = models.ForeignKey(Categories)


class Wardrobe(models.Model):
	user = models.ForeignKey(User)
	item = models.ForeignKey(Item)
	times_used = models.PositiveIntegerField(default=0)