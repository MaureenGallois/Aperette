from aperetteAPI.models import Ingredient

from django.test import TestCase


class IngredientTest(TestCase):
   def setUp(self):
      Ingredient.objects.create(nom="oeuf")

   def str_ingredient(self):
      ingredient = Ingredient.objects.get(nom="oeuf")
      self.assertEquals(ingredient.nom,str(ingredient.nom))