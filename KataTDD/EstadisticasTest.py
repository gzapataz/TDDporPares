from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular("")[0],0, "String Vacio")

    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("25")[0],1, "Ciclo un Numero")

    def test_calcular_dos_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10")[0],2, "Ciclo con dos numeros, devuelve numero de elementos")

    def test_calcular_varios_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10,12")[0],3, "Ciclo con varios numeros, devuelve numero de elementos")
