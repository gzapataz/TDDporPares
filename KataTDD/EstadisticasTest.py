from unittest import TestCase
from Estadisticas import Estadisticas


class EstadisticasTest(TestCase):
    #Paso 1 Devolver un arreglo con el numero de elementos

    #Iteracion 1
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular("")[0], 0, "String Vacio")

    # Iteracion 2
    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("25")[0], 1, "Ciclo un Numero")

    # Iteracion 3
    def test_calcular_dos_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10")[0], 2, "Ciclo con dos numeros, devuelve numero de elementos")

    # Iteracion 4
    def test_calcular_varios_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10,12")[0], 3, "Ciclo con varios numeros, devuelve numero de elementos")


    #Paso 2 Devolver un arreglo con el numero de elementos y el minimo

    # Iteracion 1
    def test_calcular_minimo(self):
        self.assertEqual(Estadisticas().calcular("")[1], 0, "String Vacio y minimo")

    # Iteracion 2
    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("25")[0],1, "Ciclo un Numero")
        self.assertEqual(Estadisticas().calcular("25")[1], 25, "Minimo un Numero")

    # Iteracion 3
    def test_calcular_dos_numeros_minimo(self):
        self.assertEqual(Estadisticas().calcular("25,10")[1], 10, "Ciclo con dos numeros, devuelve el minimo de los dos")
        self.assertEqual(Estadisticas().calcular("11,40")[1], 11, "Ciclo con dos numeros, devuelve el minimo de los dos")

    # Iteracion 4
    def test_calcular_dos_numeros_minimo(self):
        self.assertEqual(Estadisticas().calcular("25,10, 9")[1], 9, "Ciclo con varios numeros, devuelve el minimo de los dos")


