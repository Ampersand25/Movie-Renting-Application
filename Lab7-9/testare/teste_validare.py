import unittest

from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
from domeniu.data_entitate import Data
from domeniu.inchiriere_entitate import Inchiriere

from validare.validator_film import ValidatorFilm
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere

from erori.exceptii import ValidError

class TestCaseFilmValidare(unittest.TestCase):
    def testValidareFilm1(self):
        #metoda care valideaza campurile dintr-ul obiect de clasa Film

        valid = ValidatorFilm()

        film_rau = Film(-5, '', '', '', 1264, 1e+3)
        self.assertRaisesRegex(ValidError, 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\ndurata totala de rulare invalida!\n', valid.valideaza, film_rau)

    def testValidareFilm2(self):
        valid = ValidatorFilm()

        film_rau = Film(55, '', '', '', 1264, 59)
        self.assertRaisesRegex(ValidError, 'titlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\ndurata totala de rulare invalida!\n', valid.valideaza, film_rau)

    def testValidareFilm3(self):
        valid = ValidatorFilm()

        film_rau = Film(-31, '', '', '', 2020, 211)
        self.assertRaisesRegex(ValidError, 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\ndurata totala de rulare invalida!\n', valid.valideaza, film_rau)

    def testValidareFilm4(self):
        valid = ValidatorFilm()

        film_rau = Film(-1, '', '', '', 2021, 83)
        self.assertRaisesRegex(ValidError, 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\n', valid.valideaza, film_rau)

    def testValidareFilm5(self):
        valid = ValidatorFilm()

        film_rau = Film(3, '', '', '', 2016, -64)
        self.assertRaisesRegex(ValidError, 'titlu invalid!\ndescriere invalida!\ngen invalid!\ndurata totala de rulare invalida!\n', valid.valideaza, film_rau)

    def testValidareFilm6(self):
        valid = ValidatorFilm()

        film_rau = Film(3, '', '', '', -7, 210)
        self.assertRaisesRegex(ValidError, 'titlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\n', valid.valideaza, film_rau)

    def testValidareFilm7(self):
        valid = ValidatorFilm()

        film_rau = Film(-67377, '', '', '', 1901, 158)
        self.assertRaisesRegex(ValidError, 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\n', valid.valideaza, film_rau)

    def testValidareFilm8(self):
        valid = ValidatorFilm()

        film_rau = Film(0, '', '', '', 1987, 60)
        self.assertRaisesRegex(ValidError, 'titlu invalid!\ndescriere invalida!\ngen invalid!\n', valid.valideaza, film_rau)

class TestCaseClientValidare(unittest.TestCase):
    def testValidareClient1(self):
        #metoda care valideaza campurile dintr-ul obiect de clasa Client

        valid = ValidatorClient()

        client_rau = Client(-852, '', 741786776282)
        self.assertRaisesRegex(ValidError, 'id client invalid!\nnume invalid!\ncnp invalid!\n', valid.valideaza, client_rau)

    def testValidareClient2(self):
        valid = ValidatorClient()

        client_rau = Client(-46, 'Pruteanu Robert', 5011014681833)
        self.assertRaisesRegex(ValidError, 'id client invalid!\n', valid.valideaza, client_rau)

    def testValidareClient3(self):
        valid = ValidatorClient()

        client_rau = Client(61, '', 4031201300164)
        self.assertRaisesRegex(ValidError, 'nume invalid!\n', valid.valideaza, client_rau)

    def testValidareClient4(self):
        valid = ValidatorClient()

        client_rau = Client(27, 'Anton Felicia', 1e+13)
        self.assertRaisesRegex(ValidError, 'cnp invalid!\n', valid.valideaza, client_rau)

    def testValidareClient5(self):
        valid = ValidatorClient()

        client_rau = Client(-1, '', 1971030867010)
        self.assertRaisesRegex(ValidError, 'id client invalid!\nnume invalid!\n', valid.valideaza, client_rau)

    def testValidareClient6(self):
        valid = ValidatorClient()

        client_rau = Client(-96, 'Vancea Alexandru', 999999999999)
        self.assertRaisesRegex(ValidError, 'id client invalid!\ncnp invalid!\n', valid.valideaza, client_rau)

    def testValidareClient7(self):
        valid = ValidatorClient()

        client_rau = Client(0, '', -7317428638319)
        self.assertRaisesRegex(ValidError, 'nume invalid!\ncnp invalid!\n', valid.valideaza, client_rau)

class TestCaseInchiriereValidare(unittest.TestCase):
    def testValidareInchiriere1(self):
        #metoda care valideaza campurile dintr-ul obiect de clasa Inchiriere

        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(30, 10, 2010)

        inchiriere_rea = Inchiriere(4, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        film2 = Film(3, 'titlu 2', 'descriere 2', 'gen 2', 1953, 60)
        client2 = Client(17, 'nume 2', 1e+12 + 1)
        data2 = Data(14, 7, 0)

        inchiriere_rea_2 = Inchiriere(0, film2, client2, data2)
        self.assertRaisesRegex(ValidError, 'an invalid!\n', valid.valideaza, inchiriere_rea_2)

        film3 = Film(95, 'titlu 3', 'descriere 3', 'gen 3', 1899, 74)
        client3 = Client(23, 'nume 3', 1e+12 + 2)
        data3 = Data(0, 1, -6)

        inchiriere_rea_3 = Inchiriere(4, film3, client3, data3)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nan invalid!\n', valid.valideaza, inchiriere_rea_3)

        film4 = Film(73, 'titlu 4', 'descriere 4', 'gen 4', 2019, 164)
        client4 = Client(2, 'nume 4', 1e+12 + 3)
        data4 = Data(53, 9, -1)

        inchiriere_rea_4 = Inchiriere(4, film4, client4, data4)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nan invalid!\n', valid.valideaza, inchiriere_rea_4)

        film5 = Film(9, 'titlu 5', 'descriere 5', 'gen 5', 2013, 205)
        client5 = Client(1263, 'nume 5', 1e+12 + 4)
        data5 = Data(-8, 0, 2001)

        inchiriere_rea_5 = Inchiriere(539, film5, client5, data5)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nluna invalida!\n', valid.valideaza, inchiriere_rea_5)

        film6 = Film(32, 'titlu 6', 'descriere 6', 'gen 6', 1942, 153)
        client6 = Client(3, 'nume 6', 1e+12 + 5)
        data6 = Data(0, -25, -7)

        inchiriere_rea_6 = Inchiriere(284, film6, client6, data6)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nluna invalida!\nan invalid!\n', valid.valideaza, inchiriere_rea_6)

    def testValidareInchiriere2(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(10, 9, 2026)

        inchiriere_rea = Inchiriere(-1, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

        inchiriere_rea = Inchiriere(-2, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

        inchiriere_rea = Inchiriere(-3, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

        inchiriere_rea = Inchiriere(-10, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

        inchiriere_rea = Inchiriere(-78, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

        inchiriere_rea = Inchiriere(-174, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere3(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(0, 6, 2027)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere4(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(4, 0, 2021)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaisesRegex(ValidError, 'luna invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere5(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(4, 13, 2029)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nluna invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere6(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(1, 12, 2020)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere7(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(2, 12, 2020)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaises(ValidError, valid.valideaza, inchiriere_rea)

    def testValidareInchiriere8(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(30, 2, 2021)

        inchiriere_rea = Inchiriere(8, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 2, 2021)

        inchiriere_rea = Inchiriere(8, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere9(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 1, 2023)

        inchiriere_rea = Inchiriere(24, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 1, 2023)

        inchiriere_rea = Inchiriere(24, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere10(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 3, 2037)

        inchiriere_rea = Inchiriere(642, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 3, 2037)

        inchiriere_rea = Inchiriere(642, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere11(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 3, 2037)

        inchiriere_rea = Inchiriere(1963, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 3, 2037)

        inchiriere_rea = Inchiriere(1963, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere12(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(31, 4, 2094)

        inchiriere_rea = Inchiriere(28, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 4, 2094)

        inchiriere_rea = Inchiriere(28, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere13(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 5, 3016)

        inchiriere_rea = Inchiriere(43, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 5, 3016)

        inchiriere_rea = Inchiriere(43, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere14(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(31, 6, 2076)

        inchiriere_rea = Inchiriere(1, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 6, 2076)

        inchiriere_rea = Inchiriere(1, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere15(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 7, 2039)

        inchiriere_rea = Inchiriere(11, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 7, 2039)

        inchiriere_rea = Inchiriere(11, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere16(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 8, 2531)

        inchiriere_rea = Inchiriere(164, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 8, 2531)

        inchiriere_rea = Inchiriere(164, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere17(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(31, 9, 2264)

        inchiriere_rea = Inchiriere(3, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 9, 2264)

        inchiriere_rea = Inchiriere(3, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere18(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 10, 2942)

        inchiriere_rea = Inchiriere(6, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 10, 2942)

        inchiriere_rea = Inchiriere(6, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere19(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(31, 11, 2543)

        inchiriere_rea = Inchiriere(36, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 11, 2543)

        inchiriere_rea = Inchiriere(36, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere20(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(32, 12, 2034)

        inchiriere_rea = Inchiriere(11, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(0, 12, 2034)

        inchiriere_rea = Inchiriere(11, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere21(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(-4, 100, 0)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(4, 7, 2020)

        inchiriere_rea = Inchiriere(23, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(14, 11, 2019)

        inchiriere_rea = Inchiriere(85, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(1, 12, 2020)

        inchiriere_rea = Inchiriere(66, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(-4, 100, 0)

        inchiriere_rea = Inchiriere(14, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(4, 7, 2020)

        inchiriere_rea = Inchiriere(-6, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\ntermen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 2016)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza,inchiriere_rea)

        data = Data(29, 2, 2010)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 2009)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 2007)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 2006)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1600)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1601)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1602)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1603)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1604)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1900)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1901)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1902)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1903)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(29, 2, 1904)

        inchiriere_rea = Inchiriere(74, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(14, 0, 2020)

        inchiriere_rea = Inchiriere(7, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nluna invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(24, 12, 0)

        inchiriere_rea = Inchiriere(7, film, client, data)
        self.assertRaisesRegex(ValidError, 'an invalid!\n', valid.valideaza, inchiriere_rea)

    def testValidareInchiriere21BlackBox(self):
        valid = ValidatorInchiriere()

        film = Film(7, 'titlu', 'descriere', 'gen', 2020, 210)
        client = Client(3, 'nume', 1e+12)
        data = Data(-4, 100, 0)

        inchiriere_rea = Inchiriere(0, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(14, 0, 2020)

        inchiriere_rea = Inchiriere(7, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nluna invalida!\n', valid.valideaza, inchiriere_rea)

        data = Data(24, 12, 0)

        inchiriere_rea = Inchiriere(7, film, client, data)
        self.assertRaisesRegex(ValidError, 'an invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(-6, 12, 0)

        inchiriere_rea = Inchiriere(7, film, client, data)
        self.assertRaisesRegex(ValidError, 'zi invalida!\nan invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(4, 7, 2020)

        inchiriere_rea = Inchiriere(23, film, client, data)
        self.assertRaisesRegex(ValidError, 'termen de predare invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(4, 7, 2021)

        inchiriere_rea = Inchiriere(-6, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', valid.valideaza, inchiriere_rea)

        data = Data(4, 7, 2020)

        inchiriere_rea = Inchiriere(-6, film, client, data)
        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\ntermen de predare invalid!\n', valid.valideaza, inchiriere_rea)