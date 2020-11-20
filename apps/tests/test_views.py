from django.test import TestCase
from .views import registro,agregar_juego
from django.urls import reverse,resolve

class testview(TestCase):
    def test_view_registro(self):
        url = reverse('registration')
        print(resolve(url))
        self.assertEqual(resolve(url).func,registro)

    def test_view_agregar(self):
        url = reverse('agregar')
        print(resolve(url))
        self.assertEqual(resolve(url).func,agregar_juego)
