from django.contrib import admin

# Register your models here.
from user.models import Dilip


@admin.register(Dilip)
class DilipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

from .models import Recipe, Ingredient, Instruction

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ingredient', 'description')

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'description', 'description')