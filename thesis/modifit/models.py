from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class UserAvatar(models.Model):
	user_id = models.ForeignKey(User)
	shoulder = models.PositiveIntegerField(default=15)
	bust = models.PositiveIntegerField(default=34)
	waist = models.PositiveIntegerField(default=24)
	hips = models.PositiveIntegerField(default=34)
	#length = models.PositiveIntegerField(default=0)
	height = models.PositiveIntegerField(default=68)

	SKINTONE_CHOICES = (
		('W', "Warm"),
		('C', "Cool"),
		('O', "Olive"),
		('N', "Neutral"),
	)
	skintone = models.CharField(max_length=1, choices=SKINTONE_CHOICES)

class Wardrobe(models.Model):
	user_id = models.ForeignKey(User)
	item_id = models.ForeignKey(Item)
	times_used = models.PositiveIntegerField(default=0)

class Item(models.Model):
	item_name = models.CharField(max_length=100)
	shoulder = models.PositiveIntegerField(default=0)
	bust = models.PositiveIntegerField(default=0)
	waist = models.PositiveIntegerField(default=0)
	hips = models.PositiveIntegerField(default=0)
	length = models.PositiveIntegerField(default=0)

class hasColor(models.Model):
	item_id = models.ForeignKey(Item)
	red = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	green = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	blue = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])

class hasPattern(models.Model):
	item_id = models.ForeignKey(Item)
	pattern_id = models.ForeignKey(Patterns)

class Patterns(models.Model):
	pattern_name = models.CharField(max_length=100, unique=True)

class hasMaterials(models.Model):
	item_id = models.ForeignKey(Item)
	material_id = models.ForeignKey(Materials)

class Materials(models.Model):
	material_name = models.CharField(max_length=100,unique=True)

class hasCategory(models.Model):
	item_id = models.ForeignKey(Item)
	category_id = models.ForeignKey(Categories)

class Categories(models.Model):
	category_name = models.CharField(max_length=150, unique=True)