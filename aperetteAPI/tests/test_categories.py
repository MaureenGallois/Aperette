from ..models import Categorie

from django.test import TestCase


class CategorieTest(TestCase):
   def setUp(self):
      Categorie.objects.create(nom="petit four")

   def str_categorie(self):
      categorie = Categorie.objects.get(nom="petit four")
      self.assertEquals(categorie.nom,str(categorie.nom))