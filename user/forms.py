from django import forms

from .models import Dilip
class DilipForm(forms.ModelForm):
    
    class Meta:
        model = Dilip
        fields = ("name", "email", "password")
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'id':'passwordid'}),

        }


# forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'id':'titleid'}),
            # 'description': forms.Textarea(attrs={'class':'form-control, 'id':'descriptionid', 'rows':1, 'cols':15}),
            'description': forms.Textarea(attrs={"rows":5})

        }


IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=RecipeForm, extra=1)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, form=RecipeForm, extra=1)