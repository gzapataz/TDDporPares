from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular("")[0],0, "String Vacio")

    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("25")[0],1, "Ciclo un Numero")