from django.test import SimpleTestCase
from django.test import TestCase
from .forms import JuegoForm,Contacto



class testForms(SimpleTestCase):
    def test_validar_forms(self):
        form = JuegoForm(
            'nombre' == 'Company of heroes 2',
            'precio' == 9990,
            'descripcion' == 'Ambientado en la 2da guerra mundial',
            'Compañia' == 'ubisoft',
            'fecha_lanzamiento' == '01/01/2012',
            'imagen' == 'cualquierar'
        )
        self.assertTrue(form.is_valid())


class testForm(TestCase):
    def test_validar_forms(self):
        form = Contacto(
            'nombre' == 'Juan',
            'correo' == 'juan@gmai.com',
            'tipo_consulta' == 1,
            'mensaje' == 'aksjdkajskdjaksd',
            'avisos' == False,
            
        )
        self.assertTrue(form.is_valid())