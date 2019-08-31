'''
Realizado por Jose Ramos
Fecha: 31 Agosto 2019
Correo: joselowolf@gmail.com
'''

from Romanos import castRomanoToDecial
import unittest

class TestStringMethods(unittest.TestCase):
    def test_ejercicio1(self):
        romano = "I"
        assert castRomanoToDecial(romano) == 1, "Deberia ser 1"

    def test_ejercicio2(self):
        romano = "II"
        assert castRomanoToDecial(romano) == 2, "Deberia ser 2"

    def test_ejercicio4(self):
        romano = "IV"
        assert castRomanoToDecial(romano) == 4, "Deberia ser 4"

    def test_ejercicio5(self):
        romano = "V"
        assert castRomanoToDecial(romano) == 5, "Deberia ser 5"

    def test_ejercicio6(self):
        romano = "VI"
        assert castRomanoToDecial(romano) == 6, "Deberia ser 6"

    def test_ejercicio2006(self):
        romano = "MMVI"
        assert castRomanoToDecial(romano) == 2006, "Deberia ser 2006"

    def test_ejercicio1944(self):
        romano = "MCMXLIV"
        assert castRomanoToDecial(romano) == 1944, "Deberia ser 1944"

    def test_ejercicio39(self):
        romano = "XXXIX"
        assert castRomanoToDecial(romano) == 39, "Deberia ser 39"

    def test_ejercicio1903(self):
        romano = "MCMIII"
        assert castRomanoToDecial(romano) == 1903, "Deberia ser 1903"


    def test_ejercicioERROR(self):
        romano = "MCMIIIA"
        assert castRomanoToDecial(romano) == None, "No deberia ser posible transformar"

if __name__ == "__main__":
    unittest.main()