import unittest

from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
from domeniu.data_entitate import Data
from domeniu.inchiriere_entitate import Inchiriere

from infrastructura.repo_filme import RepositoryFilme
from infrastructura.repo_clienti import RepositoryClienti
from infrastructura.repo_inchirieri import RepositoryInchirieri

from business.servicii_filme import ServiceFilme
from business.servicii_clienti import ServiceClienti
from business.servicii_inchirieri import ServiceInchirieri
from business.servicii_rapoarte import ServiceRapoarte

from validare.validator_film import ValidatorFilm
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere

from erori.exceptii import ValidError

class TestCaseRapoarteServicii(unittest.TestCase):

    def testRaport1(self):
        repo_inchirieri = RepositoryInchirieri()

        client1 = Client(4, 'nume client B', 5555555555555)
        client2 = Client(7, 'nume client A', 3333333333333)
        client3 = Client(0, 'nume client D', 7777777777777)
        client4 = Client(9, 'nume client C', 1111111111111)
        client5 = Client(6, 'nume client F', 8888888888888)

        film1 = Film(13, 'titlu film 1', 'descriere film 1', 'gen film 1', 1953, 153)
        film2 = Film(7, 'titlu film 2', 'descriere film 2', 'gen film 2', 2007, 60)
        film3 = Film(21, 'titlu film 3', 'descriere film 3', 'gen film 3', 1895, 98)
        film4 = Film(1, 'titlu film 4', 'descriere film 4', 'gen film 4', 1913, 210)
        film5 = Film(5, 'titlu film 5', 'descriere film 5', 'gen film 5', 2020, 193)

        inchiriere1 = Inchiriere(7, film4, client2, Data(15, 10, 2005))
        inchiriere2 = Inchiriere(3, film2, client5, Data(8, 7, 1968))
        inchiriere3 = Inchiriere(13, film5, client5, Data(21, 1, 2013))
        inchiriere4 = Inchiriere(8, film4, client1, Data(1, 12, 2020))
        inchiriere5 = Inchiriere(1, film3, client2, Data(30, 4, 1899))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)
        repo_inchirieri.adauga(inchiriere4)
        repo_inchirieri.adauga(inchiriere5)

        srv_rapoarte = ServiceRapoarte(repo_inchirieri)

        lista_clienti = srv_rapoarte.raport_clienti_1_ordonat_nume()

        self.assertTrue(len(lista_clienti) == 3)
        self.assertEqual(lista_clienti[0], client2)
        self.assertEqual(lista_clienti[1], client1)
        self.assertEqual(lista_clienti[2], client5)

    def testRaport2(self):
        repo_inchirieri = RepositoryInchirieri()

        client1 = Client(4, 'nume client B', 5555555555555)
        client2 = Client(7, 'nume client A', 3333333333333)
        client3 = Client(0, 'nume client D', 7777777777777)
        client4 = Client(9, 'nume client C', 1111111111111)
        client5 = Client(6, 'nume client F', 8888888888888)

        film1 = Film(13, 'titlu film 1', 'descriere film 1', 'gen film 1', 1953, 153)
        film2 = Film(7, 'titlu film 2', 'descriere film 2', 'gen film 2', 2007, 60)
        film3 = Film(21, 'titlu film 3', 'descriere film 3', 'gen film 3', 1895, 98)
        film4 = Film(1, 'titlu film 4', 'descriere film 4', 'gen film 4', 1913, 210)
        film5 = Film(5, 'titlu film 5', 'descriere film 5', 'gen film 5', 2020, 193)

        inchiriere1 = Inchiriere(7, film4, client2, Data(15, 10, 2005))
        inchiriere2 = Inchiriere(3, film2, client5, Data(8, 7, 1968))
        inchiriere3 = Inchiriere(13, film5, client5, Data(21, 1, 2013))
        inchiriere4 = Inchiriere(8, film4, client1, Data(1, 12, 2020))
        inchiriere5 = Inchiriere(1, film1, client5, Data(30, 4, 1899))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)
        repo_inchirieri.adauga(inchiriere4)
        repo_inchirieri.adauga(inchiriere5)

        srv_rapoarte = ServiceRapoarte(repo_inchirieri)

        lista_clienti = srv_rapoarte.raport_clienti_1_ordonat_nr_filme()

        self.assertTrue(len(lista_clienti) == 3)
        self.assertEqual(lista_clienti[0][0], client2)
        self.assertEqual(lista_clienti[0][1], 1)
        self.assertEqual(lista_clienti[1][0], client1)
        self.assertEqual(lista_clienti[1][1], 1)
        self.assertEqual(lista_clienti[2][0], client5)
        self.assertEqual(lista_clienti[2][1], 3)

    def testRaport3(self):
        repo_inchirieri = RepositoryInchirieri()

        client1 = Client(4, 'nume client B', 5555555555555)
        client2 = Client(7, 'nume client A', 3333333333333)
        client3 = Client(0, 'nume client D', 7777777777777)
        client4 = Client(9, 'nume client C', 1111111111111)
        client5 = Client(6, 'nume client F', 8888888888888)

        film1 = Film(13, 'titlu film 1', 'descriere film 1', 'gen film 1', 1953, 153)
        film2 = Film(7, 'titlu film 2', 'descriere film 2', 'gen film 2', 2007, 60)
        film3 = Film(21, 'titlu film 3', 'descriere film 3', 'gen film 3', 1895, 98)
        film4 = Film(1, 'titlu film 4', 'descriere film 4', 'gen film 4', 1913, 210)
        film5 = Film(5, 'titlu film 5', 'descriere film 5', 'gen film 5', 2020, 193)

        inchiriere1 = Inchiriere(7, film4, client2, Data(15, 10, 2005))
        inchiriere2 = Inchiriere(3, film2, client5, Data(8, 7, 1968))
        inchiriere3 = Inchiriere(13, film5, client5, Data(21, 1, 2013))
        inchiriere4 = Inchiriere(8, film4, client1, Data(1, 12, 2020))
        inchiriere5 = Inchiriere(1, film1, client5, Data(30, 4, 1899))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)
        repo_inchirieri.adauga(inchiriere4)
        repo_inchirieri.adauga(inchiriere5)

        srv_rapoarte = ServiceRapoarte(repo_inchirieri)

        lista_filme = srv_rapoarte.raport_filme()

        self.assertTrue(len(lista_filme) == 4)
        self.assertEqual(lista_filme[0][0], film4)
        self.assertEqual(lista_filme[0][1], 2)
        self.assertEqual(lista_filme[1][0], film2)
        self.assertEqual(lista_filme[1][1], 1)
        self.assertEqual(lista_filme[2][0], film5)
        self.assertEqual(lista_filme[2][1], 1)
        self.assertEqual(lista_filme[3][0], film1)
        self.assertEqual(lista_filme[3][1], 1)

    def testRaport4(self):
        repo_inchirieri = RepositoryInchirieri()

        client1 = Client(4, 'nume client B', 5555555555555)
        client2 = Client(7, 'nume client A', 3333333333333)
        client3 = Client(0, 'nume client D', 7777777777777)
        client4 = Client(9, 'nume client C', 1111111111111)
        client5 = Client(6, 'nume client F', 8888888888888)

        film1 = Film(13, 'titlu film 1', 'descriere film 1', 'gen film 1', 1953, 153)
        film2 = Film(7, 'titlu film 2', 'descriere film 2', 'gen film 2', 2007, 60)
        film3 = Film(21, 'titlu film 3', 'descriere film 3', 'gen film 3', 1895, 98)
        film4 = Film(1, 'titlu film 4', 'descriere film 4', 'gen film 4', 1913, 210)
        film5 = Film(5, 'titlu film 5', 'descriere film 5', 'gen film 5', 2020, 193)

        inchiriere1 = Inchiriere(7, film4, client2, Data(15, 10, 2005))
        inchiriere2 = Inchiriere(3, film2, client5, Data(8, 7, 1968))
        inchiriere3 = Inchiriere(13, film5, client5, Data(21, 1, 2013))
        inchiriere4 = Inchiriere(8, film4, client1, Data(1, 12, 2020))
        inchiriere5 = Inchiriere(1, film1, client5, Data(30, 4, 1899))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)
        repo_inchirieri.adauga(inchiriere4)
        repo_inchirieri.adauga(inchiriere5)

        srv_rapoarte = ServiceRapoarte(repo_inchirieri)

        lista_clienti = srv_rapoarte.raport_clienti_2()

        self.assertTrue(len(lista_clienti) == 3)
        self.assertEqual(lista_clienti[0][0], client5)
        self.assertEqual(lista_clienti[0][1], 3)
        self.assertEqual(lista_clienti[1][0], client2)
        self.assertEqual(lista_clienti[1][1], 1)
        self.assertEqual(lista_clienti[2][0], client1)
        self.assertEqual(lista_clienti[2][1], 1)

    def testRaport5(self):
        repo_inchirieri = RepositoryInchirieri()

        client1 = Client(4, 'nume client B', 5555555555555)
        client2 = Client(7, 'nume client A', 3333333333333)
        client3 = Client(0, 'nume client D', 7777777777777)
        client4 = Client(9, 'nume client C', 1111111111111)
        client5 = Client(6, 'nume client F', 8888888888888)

        film1 = Film(13, 'titlu film 1', 'descriere film 1', 'gen film 1', 1953, 153)
        film2 = Film(7, 'titlu film 2', 'descriere film 2', 'gen film 2', 2007, 60)
        film3 = Film(21, 'titlu film 3', 'descriere film 3', 'gen film 3', 1895, 98)
        film4 = Film(1, 'titlu film 4', 'descriere film 4', 'gen film 4', 1913, 210)
        film5 = Film(5, 'titlu film 5', 'descriere film 5', 'gen film 5', 2020, 193)

        inchiriere1 = Inchiriere(7, film4, client2, Data(15, 10, 2005))
        inchiriere2 = Inchiriere(3, film2, client5, Data(8, 7, 1968))
        inchiriere3 = Inchiriere(13, film5, client5, Data(21, 1, 2013))
        inchiriere4 = Inchiriere(8, film4, client1, Data(1, 12, 2020))
        inchiriere5 = Inchiriere(1, film1, client5, Data(30, 4, 1899))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)
        repo_inchirieri.adauga(inchiriere4)
        repo_inchirieri.adauga(inchiriere5)

        srv_rapoarte = ServiceRapoarte(repo_inchirieri)

        lista_filme = srv_rapoarte.raport_filme_2()

        self.assertTrue(len(lista_filme) == 4)
        self.assertEqual(lista_filme[0], film4)
        self.assertEqual(lista_filme[1], film2)
        self.assertEqual(lista_filme[2], film5)
        self.assertEqual(lista_filme[3], film1)

class TestCaseClientiServicii(unittest.TestCase):

    def testServiceClienti1(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorClient()
        repo_clienti = RepositoryClienti()

        srv_clienti = ServiceClienti(valid, repo_clienti, repo_inchirieri)

        client = Client(4, 'Radu Florian Sava', 8888888888888)
        srv_clienti.adauga_client(client.get_id_client(), client.get_nume(), client.get_cnp())

        lista_client = srv_clienti.get_clienti()
        self.assertTrue(repo_clienti.__len__() == 1)
        self.assertTrue(len(lista_client) == 1)
        self.assertEqual(lista_client[0], client)

        client2 = Client(9, 'Dragos Spiridon', 3333333333333)
        srv_clienti.adauga_client(client2.get_id_client(), client2.get_nume(), client2.get_cnp())

        lista_client = srv_clienti.get_clienti()
        self.assertTrue(repo_clienti.__len__() == 2)
        self.assertTrue(len(lista_client) == 2)
        self.assertEqual(lista_client[0], client)
        self.assertEqual(lista_client[1], client2)

    def testServiceClienti2(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorClient()
        repo_clienti = RepositoryClienti()

        srv_clienti = ServiceClienti(valid, repo_clienti, repo_inchirieri)

        self.assertRaisesRegex(ValidError, 'id client invalid!\n', srv_clienti.cauta_client, -4)

        client = Client(4, 'Radu Florian Sava', 8888888888888)
        srv_clienti.adauga_client(client.get_id_client(), client.get_nume(), client.get_cnp())

        self.assertTrue(client == srv_clienti.cauta_client(client.get_id_client()))

        client2 = Client(9, 'Dragos Spiridon', 3333333333333)
        srv_clienti.adauga_client(client2.get_id_client(), client2.get_nume(), client2.get_cnp())

        self.assertTrue(client2 == srv_clienti.cauta_client(client2.get_id_client()))
        self.assertTrue(client == srv_clienti.cauta_client(client.get_id_client()))

    def testServiceClienti3(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorClient()
        repo_clienti = RepositoryClienti()

        srv_clienti = ServiceClienti(valid, repo_clienti, repo_inchirieri)

        client = Client(4, 'Radu Florian Sava', 8888888888888)
        srv_clienti.adauga_client(client.get_id_client(), client.get_nume(), client.get_cnp())

        client2 = Client(9, 'Dragos Spiridon', 3333333333333)
        srv_clienti.adauga_client(client2.get_id_client(), client2.get_nume(), client2.get_cnp())

        lista_clienti = srv_clienti.get_clienti()
        self.assertTrue(lista_clienti[0].get_id_client() == client.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() == client.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() == client.get_cnp())
        self.assertEqual(lista_clienti[1].get_id_client(), client2.get_id_client())
        self.assertEqual(lista_clienti[1].get_nume(), client2.get_nume())
        self.assertEqual(lista_clienti[1].get_cnp(), client2.get_cnp())

        client_nou = Client(4, 'Robert Andrei Pruteanu', 9999999999999)
        srv_clienti.modifica_client(4, 'Robert Andrei Pruteanu', 9999999999999)

        lista_clienti = srv_clienti.get_clienti()
        self.assertTrue(lista_clienti[0].get_id_client() == client.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() != client.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() != client.get_cnp())
        self.assertTrue(lista_clienti[0].get_id_client() == client_nou.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() == client_nou.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() == client_nou.get_cnp())
        self.assertEqual(lista_clienti[1].get_id_client(), client2.get_id_client())
        self.assertEqual(lista_clienti[1].get_nume(), client2.get_nume())
        self.assertEqual(lista_clienti[1].get_cnp(), client2.get_cnp())

        client_nou2 = Client(9, 'Marius Sterian', 1111111111111)
        srv_clienti.modifica_client(9, 'Marius Sterian', 1111111111111)

        self.assertTrue(lista_clienti[0].get_id_client() == client.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() != client.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() != client.get_cnp())
        self.assertTrue(lista_clienti[0].get_id_client() == client_nou.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() == client_nou.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() == client_nou.get_cnp())
        self.assertEqual(lista_clienti[1].get_id_client(), client2.get_id_client())
        self.assertTrue(lista_clienti[1].get_nume() != client2.get_nume())
        self.assertTrue(lista_clienti[1].get_cnp() != client2.get_cnp())
        self.assertEqual(lista_clienti[1].get_id_client(), client_nou2.get_id_client())
        self.assertTrue(lista_clienti[1].get_nume() == client_nou2.get_nume())
        self.assertTrue(lista_clienti[1].get_cnp() == client_nou2.get_cnp())

    def testServiceClienti4(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorClient()
        repo_clienti = RepositoryClienti()

        srv_clienti = ServiceClienti(valid, repo_clienti, repo_inchirieri)

        client = Client(4, 'Radu Florian Sava', 8888888888888)
        srv_clienti.adauga_client(client.get_id_client(), client.get_nume(), client.get_cnp())

        client2 = Client(9, 'Dragos Spiridon', 3333333333333)
        srv_clienti.adauga_client(client2.get_id_client(), client2.get_nume(), client2.get_cnp())

        self.assertRaisesRegex(ValidError, 'id client invalid!\n', srv_clienti.sterge_client, -1)

        lista_clienti = srv_clienti.get_clienti()
        self.assertTrue(len(lista_clienti) == 2)

        film1 = Film(5, 'titlu 1', 'descriere 1', 'gen 1', 1956, 205)
        film2 = Film(3, 'titlu 2', 'descriere 2', 'gen 2', 2018, 175)
        film3 = Film(8, 'titlu 3', 'descriere 3', 'gen 3', 2004, 98)

        inchiriere1 = Inchiriere(7, film2, client, Data(4, 12, 2017))
        inchiriere2 = Inchiriere(4, film1, client2, Data(13, 4, 1994))
        inchiriere3 = Inchiriere(13, film3, client, Data(11, 1, 2000))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)

        srv_clienti.sterge_client(4)

        lista_clienti = srv_clienti.get_clienti()
        self.assertTrue(len(lista_clienti) == 1)

        srv_clienti.sterge_client(9)

        lista_clienti = srv_clienti.get_clienti()
        self.assertTrue(len(lista_clienti) == 0)

    def testServiceClienti5(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorClient()
        repo_clienti = RepositoryClienti()

        srv_clienti = ServiceClienti(valid, repo_clienti, repo_inchirieri)

        nr = srv_clienti._ServiceClienti__generare_numar_random(1, 100)
        self.assertTrue(nr >= 1 and nr <= 101)

        nume = srv_clienti._ServiceClienti__generare_nume_random()
        self.assertTrue(len(nume) >= 3 and len(nume) <= 21)
        self.assertTrue(nume != '')

        srv_clienti.generare_clienti()
        self.assertTrue(repo_clienti.__len__() != 0)
        self.assertTrue(repo_clienti.__len__() >= 5)
        self.assertTrue(repo_clienti.__len__() <= 16)

        self.assertTrue(srv_clienti.nr_clienti() != 0)
        self.assertTrue(srv_clienti.nr_clienti() >= 5)
        self.assertTrue(srv_clienti.nr_clienti() <= 16)

class TestCaseFilmeServicii(unittest.TestCase):

    def testServiceFilme1(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorFilm()
        repo_filme = RepositoryFilme()

        srv_filme = ServiceFilme(valid, repo_filme, repo_inchirieri)

        film = Film(0, 'titlu 1', 'descriere 1', 'gen 1', 1942, 163)
        srv_filme.adauga_film(film.get_id_film(), film.get_titlu(), film.get_descriere(), film.get_gen(), film.get_an_lansare(), film.get_durata())

        lista_filme = srv_filme.get_filme()
        self.assertTrue(repo_filme.__len__() == 1)
        self.assertTrue(len(lista_filme) == 1)
        self.assertEqual(lista_filme[0], film)

        film_nou = Film(13, 'titlu 2', 'descriere 2', 'gen 2', 2013, 209)
        srv_filme.adauga_film(film_nou.get_id_film(), film_nou.get_titlu(), film_nou.get_descriere(), film_nou.get_gen(), film_nou.get_an_lansare(), film_nou.get_durata())

        lista_filme = srv_filme.get_filme()
        self.assertTrue(repo_filme.__len__() == 2)
        self.assertTrue(len(lista_filme) == 2)
        self.assertEqual(lista_filme[0], film)
        self.assertEqual(lista_filme[1], film_nou)

    def testServiceFilme2(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorFilm()
        repo_filme = RepositoryFilme()

        srv_filme = ServiceFilme(valid, repo_filme, repo_inchirieri)

        self.assertRaisesRegex(ValidError, 'id film invalid!\n', srv_filme.cauta_film, -2)

        film = Film(0, 'titlu 1', 'descriere 1', 'gen 1', 1942, 163)
        srv_filme.adauga_film(film.get_id_film(), film.get_titlu(), film.get_descriere(), film.get_gen(), film.get_an_lansare(), film.get_durata())

        self.assertRaisesRegex(ValidError, 'id film invalid!\n', srv_filme.cauta_film, -5)

        film2 = Film(13, 'titlu 2', 'descriere 2', 'gen 2', 2013, 209)
        srv_filme.adauga_film(film2.get_id_film(), film2.get_titlu(), film2.get_descriere(), film2.get_gen(), film2.get_an_lansare(), film2.get_durata())

        self.assertRaisesRegex(ValidError, 'id film invalid!\n', srv_filme.cauta_film, -21)

        self.assertTrue(srv_filme.cauta_film(0) == film)
        self.assertTrue(srv_filme.cauta_film(13) == film2)

    def testServiceFilme3(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorFilm()
        repo_filme = RepositoryFilme()

        srv_filme = ServiceFilme(valid, repo_filme, repo_inchirieri)

        film = Film(0, 'titlu 1', 'descriere 1', 'gen 1', 1942, 163)
        srv_filme.adauga_film(film.get_id_film(), film.get_titlu(), film.get_descriere(), film.get_gen(), film.get_an_lansare(), film.get_durata())

        film2 = Film(13, 'titlu 2', 'descriere 2', 'gen 2', 2013, 209)
        srv_filme.adauga_film(film2.get_id_film(), film2.get_titlu(), film2.get_descriere(), film2.get_gen(), film2.get_an_lansare(), film2.get_durata())

        film_nou = Film(13, 'titlu nou', 'descriere noua', 'gen nou', 1899, 194)
        srv_filme.modifica_flim(film_nou.get_id_film(), film_nou.get_titlu(), film_nou.get_descriere(), film_nou.get_gen(), film_nou.get_an_lansare(), film_nou.get_durata())

        lista_filme = srv_filme.get_filme()
        self.assertTrue(lista_filme[1].get_titlu() == film_nou.get_titlu())
        self.assertTrue(lista_filme[1].get_descriere() == film_nou.get_descriere())
        self.assertTrue(lista_filme[1].get_gen() == film_nou.get_gen())
        self.assertTrue(lista_filme[1].get_an_lansare() == film_nou.get_an_lansare())
        self.assertTrue(lista_filme[1].get_durata() == film_nou.get_durata())

    def testServiceFilme4(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorFilm()
        repo_filme = RepositoryFilme()

        srv_filme = ServiceFilme(valid, repo_filme, repo_inchirieri)

        self.assertTrue(srv_filme.nr_filme() == 0)

        film = Film(0, 'titlu 1', 'descriere 1', 'gen 1', 1942, 163)
        srv_filme.adauga_film(film.get_id_film(), film.get_titlu(), film.get_descriere(), film.get_gen(), film.get_an_lansare(), film.get_durata())

        self.assertTrue(srv_filme.nr_filme() == 1)

        film2 = Film(13, 'titlu 2', 'descriere 2', 'gen 2', 2013, 209)
        srv_filme.adauga_film(film2.get_id_film(), film2.get_titlu(), film2.get_descriere(), film2.get_gen(), film2.get_an_lansare(), film2.get_durata())

        self.assertTrue(srv_filme.nr_filme() == 2)

        self.assertRaisesRegex(ValidError, 'id film invalid!\n', srv_filme.sterge_film, -3)

        client1 = Client(8, 'nume 1', 2222222222222)
        client2 = Client(0, 'nume 2', 3333333333333)
        client3 = Client(4, 'nume 3', 4444444444444)

        inchiriere1 = Inchiriere(7, film2, client1, Data(4, 12, 2017))
        inchiriere2 = Inchiriere(4, film, client3, Data(13, 4, 1994))
        inchiriere3 = Inchiriere(13, film2, client2, Data(11, 1, 2000))

        repo_inchirieri.adauga(inchiriere1)
        repo_inchirieri.adauga(inchiriere2)
        repo_inchirieri.adauga(inchiriere3)

        self.assertTrue(srv_filme.nr_filme() == 2)

        srv_filme.sterge_film(13)

        self.assertTrue(srv_filme.nr_filme() == 1)

        srv_filme.sterge_film(0)

        self.assertTrue(srv_filme.nr_filme() == 0)

    def testServiceFilme5(self):
        repo_inchirieri = RepositoryInchirieri()

        valid = ValidatorFilm()
        repo_filme = RepositoryFilme()

        srv_filme = ServiceFilme(valid, repo_filme, repo_inchirieri)

        self.assertTrue(srv_filme.nr_filme() == 0)

        srv_filme.generare_filme()

        self.assertTrue(srv_filme.nr_filme() >= 5)
        self.assertTrue(srv_filme.nr_filme() <= 16)

class TestCaseInchirieriServicii(unittest.TestCase):

    def testServiceInchirieri1(self):
        repo_inchirieri = RepositoryInchirieri()
        repo_filme = RepositoryFilme()
        repo_clienti = RepositoryClienti()

        valid = ValidatorInchiriere()

        srv_inchirieri = ServiceInchirieri(valid, repo_inchirieri, repo_filme, repo_clienti)

        self.assertTrue(srv_inchirieri.nr_inchirieri() == 0)

        srv_inchirieri.adauga_inchirieri_repo()

        self.assertTrue(srv_inchirieri.nr_inchirieri() == 11)

    def testServiceInchirieri2(self):
        repo_inchirieri = RepositoryInchirieri()
        repo_filme = RepositoryFilme()
        repo_clienti = RepositoryClienti()

        valid = ValidatorInchiriere()

        srv_inchirieri = ServiceInchirieri(valid, repo_inchirieri, repo_filme, repo_clienti)

        srv_inchirieri.adauga_inchirieri_repo()

        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', srv_inchirieri.cauta_inchiriere, -4)
        self.assertTrue(srv_inchirieri.cauta_inchiriere(3).get_id_inchiriere() == 3)

    def testServiceInchirieri3(self):
        repo_inchirieri = RepositoryInchirieri()
        repo_filme = RepositoryFilme()
        repo_clienti = RepositoryClienti()

        valid = ValidatorInchiriere()

        srv_inchirieri = ServiceInchirieri(valid, repo_inchirieri, repo_filme, repo_clienti)

        list_inchirieri = srv_inchirieri.get_inchirieri()
        self.assertTrue(srv_inchirieri.nr_inchirieri() == 0)
        self.assertTrue(len(list_inchirieri) == 0)

        srv_inchirieri.adauga_inchirieri_repo()

        list_inchirieri = srv_inchirieri.get_inchirieri()
        self.assertTrue(srv_inchirieri.nr_inchirieri() == 11)
        self.assertTrue(len(list_inchirieri) == 11)

        self.assertRaisesRegex(ValidError, 'id inchiriere invalid!\n', srv_inchirieri.returnare_film, -1)

        srv_inchirieri.returnare_film(3)
        list_inchirieri = srv_inchirieri.get_inchirieri()
        self.assertTrue(srv_inchirieri.nr_inchirieri() == 10)
        self.assertTrue(len(list_inchirieri) == 10)

    def testServiceInchirieri4(self):
        repo_inchirieri = RepositoryInchirieri()
        repo_filme = RepositoryFilme()
        repo_clienti = RepositoryClienti()

        valid = ValidatorInchiriere()

        srv_inchirieri = ServiceInchirieri(valid, repo_inchirieri, repo_filme, repo_clienti)

        list_inchirieri = srv_inchirieri.get_inchirieri()
        self.assertTrue(srv_inchirieri.nr_inchirieri() == 0)
        self.assertTrue(len(list_inchirieri) == 0)

        srv_inchirieri.adauga_inchirieri_repo()

        srv_inchirieri.inchiriere_film(14, 3, 1, ['13', '11', '2021'])

        self.assertRaisesRegex(Exception, 'numar invalid de argumente pentru data calendaristica!\n', srv_inchirieri.inchiriere_film, 132, 0, 5, ['13', '11'])

    def testServiceInchirieri5(self):
        repo_inchirieri = RepositoryInchirieri()
        repo_filme = RepositoryFilme()
        repo_clienti = RepositoryClienti()

        valid = ValidatorInchiriere()

        srv_inchirieri = ServiceInchirieri(valid, repo_inchirieri, repo_filme, repo_clienti)

        list_inchirieri = srv_inchirieri.get_inchirieri()
        self.assertTrue(srv_inchirieri.nr_inchirieri() == 0)
        self.assertTrue(len(list_inchirieri) == 0)

        srv_inchirieri.adauga_inchirieri_repo()

        srv_inchirieri.inchiriere_film(14, 3, 1, ['13', '11', '2021'])

        self.assertRaisesRegex(Exception, 'numar invalid de argumente pentru data calendaristica!\n', srv_inchirieri.modifica_inchiriere, 14, 8, 1, ['13'])

        srv_inchirieri.modifica_inchiriere(14, 0, 8, ['5', '8', '2043'])