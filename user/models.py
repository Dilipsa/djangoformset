from django.db import models


class Dilip(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    Ingredient = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.Ingredient)
    

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.recipe)
    