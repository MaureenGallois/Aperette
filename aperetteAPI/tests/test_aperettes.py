
from aperetteAPI.models import Aperette, Categorie

from django.test import TestCase


class AperetteTest(TestCase):
   def setUp(self):
      aperetteCreate = Aperette.objects.create(nom="mini quiches",photo="",recette=False,proportions=1,alcoolAssocie="rum")
      categories = aperetteCreate.categories.create(nom="petit four")

   def str_aperette(self):
      aperette = Aperette.objects.get(nom="mini quiches")
      self.assertEquals(aperette.nom,str(aperette.nom))