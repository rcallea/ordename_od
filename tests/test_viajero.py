from unittest import TestCase

from src.ordename_od.viajero import Viajero


class TestViajero(TestCase):
    def test_get_nombre(self):
        viajero = Viajero("Rubby", "Casallas G.", "rubby.casallas@gmail.com")
        assert viajero.get_nombre()=="Rubby"
