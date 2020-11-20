from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.registro_url=reverse('registro')


        return super().setUp()

class RegistroTest(BaseTest):
    def test_can_view_page_correctly(self):
        response=self.client.get(self.registro_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/registro.html')