import unittest

from erori.exceptii import RepoError

from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
from domeniu.data_entitate import Data
from domeniu.inchiriere_entitate import Inchiriere

from infrastructura.repo_filme import RepositoryFilme
from infrastructura.repo_clienti import RepositoryClienti
from infrastructura.repo_inchirieri import RepositoryInchirieri

from infrastructura.file_repo_filme import FileRepositoryFilme
from infrastructura.file_repo_clienti import FileRepositoryClienti
from infrastructura.file_repo_inchirieri import FileRepositoryInchirieri

class TestCaseRepoClienti(unittest.TestCase):

    def testRepoClienti1(self):
        repo_clienti = RepositoryClienti()
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 0)
        self.assertEqual(len(lista_clienti), 0)
        self.assertEqual(lista_clienti, [])

        client = Client(4, 'Gabriel Mircea', 3842164327542)
        repo_clienti.adauga(client)
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 1)
        self.assertEqual(len(lista_clienti), 1)
        self.assertEqual(lista_clienti[0], client)

        client = Client(4, 'Radu Florian Sava', 1742859205153)
        self.assertRaisesRegex(RepoError, 'client deja existent!\n', repo_clienti.adauga, client)
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 1)
        self.assertEqual(len(lista_clienti), 1)
        self.assertEqual(lista_clienti[0], client)

        client = Client(2, 'Dragos Spiridon', 3842164327542)
        self.assertRaisesRegex(RepoError, 'client deja existent!\n', repo_clienti.adauga, client)
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 1)
        self.assertEqual(len(lista_clienti), 1)
        self.assertEqual(lista_clienti[0], client)

        client = Client(4, 'Dragos Spiridon', 3842164327542)
        self.assertRaisesRegex(RepoError, 'client deja existent!\n', repo_clienti.adauga, client)
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 1)
        self.assertEqual(len(lista_clienti), 1)
        self.assertEqual(lista_clienti[0], client)

        client2 = Client(0, 'Robert Andrei Pruteanu', 9628421753824)
        repo_clienti.adauga(client2)
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 2)
        self.assertEqual(len(lista_clienti), 2)
        self.assertEqual(lista_clienti[0], client)
        self.assertEqual(lista_clienti[1], client2)

        client3 = Client(13, 'Norbert Roszinecs', 3815428247184)
        repo_clienti.adauga(client3)
        lista_clienti = repo_clienti.get_all()
        self.assertEqual(repo_clienti.__len__(), 3)
        self.assertEqual(len(lista_clienti), 3)
        self.assertEqual(lista_clienti[0], client)
        self.assertEqual(lista_clienti[1], client2)
        self.assertEqual(lista_clienti[2], client3)

    def testRepoClienti2(self):
        repo_clienti = RepositoryClienti()

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 4)

        client = Client(4, 'Gabriel Mircea', 3842164327542)
        repo_clienti.adauga(client)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 0)

        self.assertEqual(client, repo_clienti.cauta_dupa_id(4))

        client2 = Client(0, 'Robert Andrei Pruteanu', 9628421753824)
        repo_clienti.adauga(client2)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 1)

        self.assertEqual(client, repo_clienti.cauta_dupa_id(4))
        self.assertEqual(client2, repo_clienti.cauta_dupa_id(0))

        client3 = Client(13, 'Norbert Roszinecs', 3815428247184)
        repo_clienti.adauga(client3)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 1)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 12)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.cauta_dupa_id, 14)

        self.assertEqual(client, repo_clienti.cauta_dupa_id(4))
        self.assertEqual(client2, repo_clienti.cauta_dupa_id(0))
        self.assertEqual(client3, repo_clienti.cauta_dupa_id(13))

    def testRepoClienti3(self):
        repo_clienti = RepositoryClienti()

        client_nou = Client(0, 'Radu Florian Sava', 6472842853243)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.modifica, client_nou)

        client = Client(4, 'Gabriel Mircea', 3842164327542)
        repo_clienti.adauga(client)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.modifica, client_nou)

        client2 = Client(0, 'Robert Andrei Pruteanu', 9628421753824)
        repo_clienti.adauga(client2)

        repo_clienti.modifica(client_nou)

        client3 = Client(13, 'Norbert Roszinecs', 3815428247184)
        repo_clienti.adauga(client3)

        client_nou_2 = Client(3, 'Vlad Mircea', 1748295201604)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.modifica, client_nou_2)

        lista_clienti = repo_clienti.get_all()
        self.assertEqual(lista_clienti[0].get_id_client(), client.get_id_client())
        self.assertEqual(lista_clienti[0].get_nume(), client.get_nume())
        self.assertEqual(lista_clienti[0].get_cnp(), client.get_cnp())

        self.assertEqual(lista_clienti[1].get_id_client(), client_nou.get_id_client())
        self.assertEqual(lista_clienti[1].get_nume(), client_nou.get_nume())
        self.assertEqual(lista_clienti[1].get_cnp(), client_nou.get_cnp())

        self.assertEqual(lista_clienti[2].get_id_client(), client3.get_id_client())
        self.assertEqual(lista_clienti[2].get_nume(), client3.get_nume())
        self.assertEqual(lista_clienti[2].get_cnp(), client3.get_cnp())

    def testRepoClienti4(self):
        repo_clienti = RepositoryClienti()

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 2)

        client = Client(4, 'Gabriel Mircea', 3842164327542)
        repo_clienti.adauga(client)
        self.assertEqual(repo_clienti.__len__(), 1)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 5)

        client2 = Client(0, 'Robert Andrei Pruteanu', 9628421753824)
        repo_clienti.adauga(client2)
        self.assertEqual(repo_clienti.__len__(), 2)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 1)

        client3 = Client(13, 'Norbert Roszinecs', 3815428247184)
        repo_clienti.adauga(client3)
        self.assertEqual(repo_clienti.__len__(), 3)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 1)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 12)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', repo_clienti.sterge_dupa_id, 14)

        repo_clienti.sterge_dupa_id(0)

        self.assertEqual(repo_clienti.__len__(), 2)

        repo_clienti.sterge_dupa_id(13)

        self.assertEqual(repo_clienti.__len__(), 1)

        repo_clienti.sterge_dupa_id(4)

        self.assertEqual(repo_clienti.__len__(), 0)

class TestCaseRepoFilme(unittest.TestCase):

    def testRepoFilme1(self):
        repo_filme = RepositoryFilme()
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 0)
        self.assertEqual(len(lista_filme), 0)
        self.assertEqual(lista_filme, [])

        film = Film(8, 'titlu', 'descriere', 'gen', 1963, 124)
        repo_filme.adauga(film)
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 1)
        self.assertEqual(len(lista_filme), 1)
        self.assertEqual(lista_filme[0], film)

        film = Film(8, 'titlu nou', 'descriere noua', 'gen nou', 1946, 89)
        self.assertRaisesRegex(RepoError, 'film deja existent!\n', repo_filme.adauga, film)
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 1)
        self.assertEqual(len(lista_filme), 1)
        self.assertEqual(lista_filme[0], film)

        film2 = Film(0, 'titlu 2', 'descriere 2', 'gen 2', 2016, 205)
        repo_filme.adauga(film2)
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 2)
        self.assertEqual(len(repo_filme), 2)
        self.assertEqual(lista_filme[0], film)
        self.assertEqual(lista_filme[1], film2)

        film3 = Film(21, 'titlu 3', 'descriere 3', 'gen 3', 2007, 198)
        repo_filme.adauga(film3)
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 3)
        self.assertEqual(len(repo_filme), 3)
        self.assertEqual(lista_filme[0], film)
        self.assertEqual(lista_filme[1], film2)
        self.assertEqual(lista_filme[2], film3)

        film4 = Film(15, 'titlu 4', 'descriere 4', 'gen 4', 1998, 210)
        repo_filme.adauga(film4)
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 4)
        self.assertEqual(len(repo_filme), 4)
        self.assertEqual(lista_filme[0], film)
        self.assertEqual(lista_filme[1], film2)
        self.assertEqual(lista_filme[2], film3)
        self.assertEqual(lista_filme[3], film4)

        film5 = Film(10, 'titlu 5', 'descriere 5', 'gen 5', 2020, 60)
        repo_filme.adauga(film5)
        lista_filme = repo_filme.get_all()
        self.assertEqual(repo_filme.__len__(), 5)
        self.assertEqual(len(repo_filme), 5)
        self.assertEqual(lista_filme[0], film)
        self.assertEqual(lista_filme[1], film2)
        self.assertEqual(lista_filme[2], film3)
        self.assertEqual(lista_filme[3], film4)
        self.assertEqual(lista_filme[4], film5)

    def testRepoFilme2(self):
        repo_filme = RepositoryFilme()

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 0)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 1)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 10)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 50)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 100)

        film = Film(8, 'titlu', 'descriere', 'gen', 1963, 124)
        repo_filme.adauga(film)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 9)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 0)

        self.assertEqual(film, repo_filme.cauta_dupa_id(8))

        film2 = Film(0, 'titlu 2', 'descriere 2', 'gen 2', 2016, 205)
        repo_filme.adauga(film2)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 9)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 1)

        self.assertEqual(film, repo_filme.cauta_dupa_id(8))
        self.assertEqual(film2, repo_filme.cauta_dupa_id(0))

        film3 = Film(21, 'titlu 3', 'descriere 3', 'gen 3', 2007, 198)
        repo_filme.adauga(film3)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 9)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 1)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 20)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.cauta_dupa_id, 22)

        self.assertEqual(film, repo_filme.cauta_dupa_id(8))
        self.assertEqual(film2, repo_filme.cauta_dupa_id(0))
        self.assertEqual(film3, repo_filme.cauta_dupa_id(21))

    def testRepoFilme3(self):
        repo_filme = RepositoryFilme()

        film_nou = Film(6, 'titlu nou', 'descriere noua', 'gen nou', 1956, 100)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.modifica, film_nou)

        film = Film(8, 'titlu', 'descriere', 'gen', 1963, 124)
        repo_filme.adauga(film)
        lista_filme = repo_filme.get_all()
        self.assertEqual(lista_filme[0].get_id_film(), film.get_id_film())
        self.assertEqual(lista_filme[0].get_titlu(), film.get_titlu())
        self.assertEqual(lista_filme[0].get_descriere(), film.get_descriere())
        self.assertEqual(lista_filme[0].get_gen(), film.get_gen())
        self.assertEqual(lista_filme[0].get_an_lansare(), film.get_an_lansare())
        self.assertEqual(lista_filme[0].get_durata(), film.get_durata())

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.modifica, film_nou)

        lista_filme = repo_filme.get_all()
        self.assertEqual(lista_filme[0], film)

        film_nou = Film(film.get_id_film(), 'titlu nou', 'descriere noua', 'gen nou', 1956, 100)
        repo_filme.modifica(film_nou)
        lista_filme = repo_filme.get_all()
        self.assertEqual(lista_filme[0].get_id_film(), film_nou.get_id_film())
        self.assertEqual(lista_filme[0].get_titlu(), film_nou.get_titlu())
        self.assertEqual(lista_filme[0].get_descriere(), film_nou.get_descriere())
        self.assertEqual(lista_filme[0].get_gen(), film_nou.get_gen())
        self.assertEqual(lista_filme[0].get_an_lansare(), film_nou.get_an_lansare())
        self.assertEqual(lista_filme[0].get_durata(), film_nou.get_durata())

        self.assertTrue(lista_filme[0].get_titlu() != 'titlu')
        self.assertTrue(lista_filme[0].get_descriere() != 'descriere')
        self.assertTrue(lista_filme[0].get_gen() != 'gen')
        self.assertTrue(lista_filme[0].get_an_lansare() != 1963)
        self.assertTrue(lista_filme[0].get_durata() != 124)

    def testRepoFilme4(self):
        repo_filme = RepositoryFilme()

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 0)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 13)

        film = Film(8, 'titlu', 'descriere', 'gen', 1963, 124)
        repo_filme.adauga(film)
        self.assertEqual(repo_filme.__len__(), 1)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 9)

        film2 = Film(0, 'titlu 2', 'descriere 2', 'gen 2', 2016, 205)
        repo_filme.adauga(film2)
        self.assertEqual(repo_filme.__len__(), 2)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 9)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 1)

        film3 = Film(21, 'titlu 3', 'descriere 3', 'gen 3', 2007, 198)
        repo_filme.adauga(film3)
        self.assertEqual(repo_filme.__len__(), 3)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 9)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 1)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 20)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', repo_filme.sterge_dupa_id, 22)

        repo_filme.sterge_dupa_id(21)

        self.assertEqual(repo_filme.__len__(), 2)

        repo_filme.sterge_dupa_id(8)

        self.assertEqual(repo_filme.__len__(), 1)

        repo_filme.sterge_dupa_id(0)

        self.assertEqual(repo_filme.__len__(), 0)

class TestCaseRepoInchirieri(unittest.TestCase):

    def testRepoInchirieri1(self):
        repo_inchirieri = RepositoryInchirieri()
        lista_inchirieri = repo_inchirieri.get_all()
        self.assertTrue(not len(lista_inchirieri))
        self.assertTrue(lista_inchirieri == [])
        self.assertTrue(not repo_inchirieri.__len__())

        self.assertEqual(len(lista_inchirieri), 0)
        self.assertEqual(lista_inchirieri, [])
        self.assertEqual(repo_inchirieri.__len__(), 0)

    def testRepoInchirieri2(self):
        repo_inchirieri = RepositoryInchirieri()

        film = Film(7, 'titlu', 'descriere', 'gen', 2019, 136)
        client = Client(15, 'nume client', 8421975382491)
        data = Data(17, 9, 2027)
        inchiriere = Inchiriere(4, film, client, data)

        repo_inchirieri.adauga(inchiriere)

        lista_inchirieri = repo_inchirieri.get_all()
        self.assertTrue(repo_inchirieri.__len__() == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere)

        film_nou = Film(0, 'titlu nou', 'descriere noua', 'gen nou', 1993, 204)
        client_nou = Client(86, 'nume client nou', 3819532193482)
        data_noua = Data(23, 11, 2021)
        inchiriere_noua = Inchiriere(4, film_nou, client_nou, data_noua)

        self.assertRaisesRegex(RepoError, 'inchiriere deja existenta!\n', repo_inchirieri.adauga, inchiriere_noua)

        inchiriere_noua = Inchiriere(11, film_nou, client_nou, data_noua)

        repo_inchirieri.adauga(inchiriere_noua)

        lista_inchirieri = repo_inchirieri.get_all()
        self.assertTrue(repo_inchirieri.__len__() == 2)
        self.assertTrue(lista_inchirieri[0] == inchiriere)
        self.assertTrue(lista_inchirieri[1] == inchiriere_noua)

        self.assertRaisesRegex(RepoError, 'inchiriere deja existenta!\n', repo_inchirieri.adauga, inchiriere_noua)

        inchiriere_noua = Inchiriere(4, film_nou, client_nou, data_noua)

        self.assertRaisesRegex(RepoError, 'inchiriere deja existenta!\n', repo_inchirieri.adauga, inchiriere_noua)

    def testRepoInchirieri3(self):
        repo_inchirieri = RepositoryInchirieri()

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.cauta_dupa_id, 7)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.cauta_dupa_id, 0)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.cauta_dupa_id, 1000)

        film = Film(7, 'titlu', 'descriere', 'gen', 2019, 136)
        client = Client(15, 'nume client', 8421975382491)
        data = Data(17, 9, 2027)
        inchiriere = Inchiriere(4, film, client, data)

        repo_inchirieri.adauga(inchiriere)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.cauta_dupa_id, 6)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.cauta_dupa_id, 8)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.cauta_dupa_id, 0)

        self.assertEqual(repo_inchirieri.cauta_dupa_id(4), inchiriere)

    def testRepoInchirieri4(self):
        repo_inchirieri = RepositoryInchirieri()

        film = Film(7, 'titlu', 'descriere', 'gen', 2019, 136)
        client = Client(15, 'nume client', 8421975382491)
        data = Data(17, 9, 2027)
        inchiriere = Inchiriere(4, film, client, data)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.modifica, inchiriere)

        repo_inchirieri.adauga(inchiriere)
        self.assertTrue(inchiriere.get_id_inchiriere() == 4)
        self.assertTrue(inchiriere.get_client() == client)
        self.assertTrue(inchiriere.get_film() == film)
        self.assertTrue(inchiriere.get_data() == data)

        film_nou = Film(13, 'titlu nou', 'descriere nou', 'gen nou', 1987, 201)
        client_nou = Client(0, 'nume client nou', 6328194281742)
        data_nou = Data(7, 12, 2021)
        inchiriere_noua = Inchiriere(1, film_nou, client_nou, data_nou)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.modifica, inchiriere_noua)

        inchiriere_noua = Inchiriere(4, film_nou, client_nou, data_nou)
        repo_inchirieri.modifica(inchiriere_noua)
        self.assertTrue(inchiriere.get_id_inchiriere() == 4)
        self.assertTrue(inchiriere.get_client() == client_nou)
        self.assertTrue(inchiriere.get_film() == film_nou)
        self.assertTrue(inchiriere.get_data() == data_nou)

    def testRepoInchirieri5(self):
        repo_inchirieri = RepositoryInchirieri()

        film = Film(7, 'titlu', 'descriere', 'gen', 2019, 136)
        client = Client(15, 'nume client', 8421975382491)
        data = Data(17, 9, 2027)
        inchiriere = Inchiriere(4, film, client, data)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 0)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 73)

        repo_inchirieri.adauga(inchiriere)
        self.assertTrue(inchiriere.get_id_inchiriere() == 4)
        self.assertTrue(inchiriere.get_client() == client)
        self.assertTrue(inchiriere.get_film() == film)
        self.assertTrue(inchiriere.get_data() == data)

        lista_inchirieri = repo_inchirieri.get_all()
        self.assertTrue(len(lista_inchirieri) == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere)
        self.assertTrue(repo_inchirieri.__len__() == 1)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 0)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 3)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 5)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', repo_inchirieri.sterge_dupa_id, 73)

        repo_inchirieri.sterge_dupa_id(4)

        lista_inchirieri = repo_inchirieri.get_all()
        self.assertTrue(len(lista_inchirieri) == 0)
        self.assertTrue(lista_inchirieri == [])
        self.assertTrue(repo_inchirieri.__len__() == 0)

class TestCaseFileRepoClienti(unittest.TestCase):

    def testFileRepoClienti1(self):
        filename = 'test_clienti.txt'
        file = open(filename, 'w')

        file_repo_clienti = FileRepositoryClienti(filename)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 0)
        self.assertTrue(lista_clienti == [])
        self.assertTrue(len(lista_clienti) == 0)

        file_repo_clienti._FileRepositoryClienti__citeste_tot_din_fisier()
        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 0)
        self.assertTrue(lista_clienti == [])
        self.assertTrue(len(lista_clienti) == 0)

        client = Client(9, 'Robert Andrei Prute', 1638195306420)

        file_repo_clienti._FileRepositoryClienti__append_client_fisier(client)

        file_repo_clienti._FileRepositoryClienti__scrie_tot_in_fisier()

        file.close()

    def testFileRepoClienti2(self):
        filename = 'test_clienti.txt'
        file = open(filename, 'w')

        file_repo_clienti = FileRepositoryClienti(filename)

        client = Client(9, 'Robert Andrei Prute', 1638195306420)

        file_repo_clienti.adauga(client)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 1)
        self.assertTrue(lista_clienti[0] == client)
        self.assertTrue(len(lista_clienti) == 1)

        client_nou = Client(9, 'Dragos Spiri', 8539164884921)

        self.assertRaisesRegex(RepoError, 'client deja existent!\n', file_repo_clienti.adauga, client_nou)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 1)
        self.assertTrue(lista_clienti[0] == client)
        self.assertTrue(len(lista_clienti) == 1)

        file.close()

    def testFileRepoClienti3(self):
        filename = 'test_clienti.txt'
        file = open(filename, 'w')

        file_repo_clienti = FileRepositoryClienti(filename)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.cauta_dupa_id, 9)

        client = Client(9, 'Robert Andrei Prute', 1638195306420)

        file_repo_clienti.adauga(client)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.cauta_dupa_id, 8)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.cauta_dupa_id, 10)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.cauta_dupa_id, 5)

        self.assertEqual(file_repo_clienti.cauta_dupa_id(9), client)

        file.close()

    def testFileRepoClienti4(self):
        filename = 'test_clienti.txt'
        file = open(filename, 'w')

        file_repo_clienti = FileRepositoryClienti(filename)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.sterge_dupa_id, 9)

        client = Client(9, 'Robert Andrei Prute', 1638195306420)

        file_repo_clienti.adauga(client)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.sterge_dupa_id, 8)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.sterge_dupa_id, 10)
        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.sterge_dupa_id, 5)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 1)
        self.assertTrue(lista_clienti[0] == client)
        self.assertTrue(lista_clienti[0].get_id_client() == client.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() == client.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() == client.get_cnp())
        self.assertTrue(len(lista_clienti) == 1)

        file_repo_clienti.sterge_dupa_id(9)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 0)
        self.assertTrue(lista_clienti == [])
        self.assertTrue(len(lista_clienti) == 0)

        file.close()

    def testFileRepoClienti5(self):
        filename = 'test_clienti.txt'
        file = open(filename, 'w')

        file_repo_clienti = FileRepositoryClienti(filename)

        client_nou = Client(13, 'Dragos Spiri', 8642953718429)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.modifica, client_nou)

        client = Client(9, 'Robert Andrei Prute', 1638195306420)

        file_repo_clienti.adauga(client)

        self.assertRaisesRegex(RepoError, 'client inexistent!\n', file_repo_clienti.modifica, client_nou)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 1)
        self.assertTrue(lista_clienti[0] == client)
        self.assertTrue(lista_clienti[0].get_id_client() == client.get_id_client())
        self.assertTrue(lista_clienti[0].get_nume() == client.get_nume())
        self.assertTrue(lista_clienti[0].get_cnp() == client.get_cnp())
        self.assertTrue(len(lista_clienti) == 1)

        client_nou = Client(9, 'Dragos Spiri', 8642953718429)

        file_repo_clienti.modifica(client_nou)

        lista_clienti = file_repo_clienti.get_all()
        self.assertTrue(file_repo_clienti.__len__() == 1)
        self.assertTrue(lista_clienti[0] == client_nou)
        self.assertTrue(len(lista_clienti) == 1)

        file.close()

class TestCaseFileRepoFilme(unittest.TestCase):

    def testFileRepoFilme1(self):
        filename = 'test_filme.txt'
        file = open(filename, 'w')

        file_repo_filme = FileRepositoryFilme(filename)

        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 0)
        self.assertTrue(lista_filme == [])
        self.assertTrue(len(lista_filme) == 0)

        file_repo_filme._FileRepositoryFilme__citeste_tot_din_fisier()
        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 0)
        self.assertTrue(lista_filme == [])
        self.assertTrue(len(lista_filme) == 0)

        film = Film(74, 'titlu', 'descriere', 'gen', 1975, 209)

        file_repo_filme._FileRepositoryFilme__append_film_fisier(film)

        file_repo_filme._FileRepositoryFilme__scrie_tot_in_fisier()

        file.close()

    def testFileRepoFilme2(self):
        filename = 'test_filme.txt'
        file = open(filename, 'w')

        file_repo_filme = FileRepositoryFilme(filename)

        film = Film(74, 'titlu', 'descriere', 'gen', 1975, 209)

        file_repo_filme.adauga(film)

        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 1)
        self.assertTrue(lista_filme[0] == film)
        self.assertTrue(len(lista_filme) == 1)

        film_nou = Film(74, 'titlu nou', 'descriere noua', 'gen nou', 2006, 136)

        self.assertRaisesRegex(RepoError, 'film deja existent!\n', file_repo_filme.adauga, film_nou)

        lista_clienti = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 1)
        self.assertTrue(lista_clienti[0] == film)
        self.assertTrue(len(lista_clienti) == 1)

        file.close()

    def testFileRepoFilme3(self):
        filename = 'test_filme.txt'
        file = open(filename, 'w')

        file_repo_filme = FileRepositoryFilme(filename)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.cauta_dupa_id, 0)

        film = Film(0, 'titlu', 'descriere', 'gen', 1895, 62)

        file_repo_filme.adauga(film)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.cauta_dupa_id, 1)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.cauta_dupa_id, 2)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.cauta_dupa_id, 3)

        self.assertEqual(file_repo_filme.cauta_dupa_id(0), film)

        file.close()

    def testFileRepoFilme4(self):
        filename = 'test_filme.txt'
        file = open(filename, 'w')

        file_repo_filme = FileRepositoryFilme(filename)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.sterge_dupa_id, 252)

        film = Film(252, 'titlu', 'descriere', 'gen', 1921, 143)

        file_repo_filme.adauga(film)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.sterge_dupa_id, 251)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.sterge_dupa_id, 253)
        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.sterge_dupa_id, 0)

        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 1)
        self.assertTrue(lista_filme[0] == film)
        self.assertTrue(lista_filme[0].get_id_film() == film.get_id_film())
        self.assertTrue(lista_filme[0].get_titlu() == film.get_titlu())
        self.assertTrue(lista_filme[0].get_descriere() == film.get_descriere())
        self.assertTrue(lista_filme[0].get_gen() == film.get_gen())
        self.assertTrue(lista_filme[0].get_an_lansare() == film.get_an_lansare())
        self.assertTrue(lista_filme[0].get_durata() == film.get_durata())
        self.assertTrue(len(lista_filme) == 1)

        file_repo_filme.sterge_dupa_id(252)

        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 0)
        self.assertTrue(lista_filme == [])
        self.assertTrue(len(lista_filme) == 0)

        file.close()

    def testFileRepoFilme5(self):
        filename = 'test_filme.txt'
        file = open(filename, 'w')

        file_repo_filme = FileRepositoryFilme(filename)

        film_nou = Film(8, 'titlu nou', 'descriere noua', 'gen nou', 1941, 210)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.modifica, film_nou)

        film = Film(0, 'titlu', 'descriere', 'gen', 2019, 60)

        file_repo_filme.adauga(film)

        self.assertRaisesRegex(RepoError, 'film inexistent!\n', file_repo_filme.modifica, film_nou)

        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 1)
        self.assertTrue(lista_filme[0] == film)
        self.assertTrue(lista_filme[0].get_id_film() == film.get_id_film())
        self.assertTrue(lista_filme[0].get_titlu() == film.get_titlu())
        self.assertTrue(lista_filme[0].get_descriere() == film.get_descriere())
        self.assertTrue(lista_filme[0].get_gen() == film.get_gen())
        self.assertTrue(lista_filme[0].get_an_lansare() == film.get_an_lansare())
        self.assertTrue(lista_filme[0].get_durata() == film.get_durata())
        self.assertTrue(len(lista_filme) == 1)

        film_nou = Film(0, 'titlu nou', 'descriere noua', 'gen nou', 1941, 210)

        file_repo_filme.modifica(film_nou)

        lista_filme = file_repo_filme.get_all()
        self.assertTrue(file_repo_filme.__len__() == 1)
        self.assertTrue(lista_filme[0] == film_nou)
        self.assertTrue(len(lista_filme) == 1)

        file.close()

class TestCaseFileRepoInchirieri(unittest.TestCase):

    def testFileRepoInchirieri1(self):
        filename = 'test_inchirieri.txt'
        file = open(filename, 'w')

        file_repo_inchirieri = FileRepositoryInchirieri(filename)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 0)
        self.assertTrue(lista_inchirieri == [])
        self.assertTrue(len(lista_inchirieri) == 0)

        file_repo_inchirieri._FileRepositoryInchirieri__citeste_tot_din_fisier()
        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 0)
        self.assertTrue(lista_inchirieri == [])
        self.assertTrue(len(lista_inchirieri) == 0)

        film = Film(7, 'titlu', 'descriere', 'gen', 1996, 165)
        client = Client(42, 'nume client', 7482916472842)
        data = Data(13, 7, 2016)
        inchiriere = Inchiriere(5, film, client, data)

        file_repo_inchirieri._FileRepositoryInchirieri__append_inchiriere_fisier(inchiriere)

        file_repo_inchirieri._FileRepositoryInchirieri__scrie_tot_in_fisier()

        file.close()

    def testFileRepoInchirieri2(self):
        filename = 'test_inchirieri.txt'
        file = open(filename, 'w')

        file_repo_inchirieri = FileRepositoryInchirieri(filename)

        film = Film(7, 'titlu', 'descriere', 'gen', 1996, 165)
        client = Client(42, 'nume client', 7482916472842)
        data = Data(13, 7, 2016)
        inchiriere = Inchiriere(81, film, client, data)

        file_repo_inchirieri.adauga(inchiriere)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere)
        self.assertTrue(len(lista_inchirieri) == 1)

        film_nou = Film(31, 'titlu nou', 'descriere noua', 'gen nou', 2015, 94)
        client_nou = Client(42, 'nume client', 5372842174210)
        data_noua = Data(1, 11, 2009)
        inchiriere_noua = Inchiriere(81, film_nou, client_nou, data_noua)

        self.assertRaisesRegex(RepoError, 'inchiriere deja existenta!\n', file_repo_inchirieri.adauga, inchiriere_noua)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere)
        self.assertTrue(len(lista_inchirieri) == 1)

        file.close()

    def testFileRepoInchirieri3(self):
        filename = 'test_inchirieri.txt'
        file = open(filename, 'w')

        file_repo_inchirieri = FileRepositoryInchirieri(filename)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.cauta_dupa_id, 25)

        film = Film(163, 'titlu', 'descriere', 'gen', 2000, 201)
        client = Client(0, 'nume client', 3849253185391)
        data = Data(21, 10, 1896)
        inchiriere = Inchiriere(25, film, client, data)

        file_repo_inchirieri.adauga(inchiriere)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.cauta_dupa_id, 24)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.cauta_dupa_id, 26)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.cauta_dupa_id, 0)

        self.assertEqual(file_repo_inchirieri.cauta_dupa_id(25), inchiriere)

        file.close()

    def testFileRepoInchirieri4(self):
        filename = 'test_inchirieri.txt'
        file = open(filename, 'w')

        file_repo_inchirieri = FileRepositoryInchirieri(filename)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.sterge_dupa_id, 7)

        film = Film(84, 'titlu', 'descriere', 'gen', 2020, 166)
        client = Client(13, 'nume client', 1953274180438)
        data = Data(30, 4, 1903)
        inchiriere = Inchiriere(7, film, client, data)

        file_repo_inchirieri.adauga(inchiriere)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.sterge_dupa_id, 6)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.sterge_dupa_id, 8)
        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.sterge_dupa_id, 9)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere)
        self.assertTrue(lista_inchirieri[0].get_film() == film)
        self.assertTrue(lista_inchirieri[0].get_client() == client)
        self.assertTrue(lista_inchirieri[0].get_data() == data)
        self.assertTrue(len(lista_inchirieri) == 1)

        file_repo_inchirieri.sterge_dupa_id(7)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 0)
        self.assertTrue(lista_inchirieri == [])
        self.assertTrue(len(lista_inchirieri) == 0)

        file.close()

    def testFileRepoInchirieri5(self):
        filename = 'test_inchirieri.txt'
        file = open(filename, 'w')

        file_repo_inchirieri = FileRepositoryInchirieri(filename)

        film_nou = Film(5, 'titlu', 'descriere', 'gen', 1958, 81)
        client_nou = Client(13, 'nume client', 7473819438123)
        data_noua = Data(28, 11, 1914)
        inchiriere_noua = Inchiriere(24, film_nou, client_nou, data_noua)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.modifica, inchiriere_noua)

        film = Film(9, 'titlu', 'descriere', 'gen', 2014, 174)
        client = Client(654, 'nume client', 9318421394183)
        data = Data(18, 6, 1974)
        inchiriere = Inchiriere(53, film, client, data)

        file_repo_inchirieri.adauga(inchiriere)

        self.assertRaisesRegex(RepoError, 'inchiriere inexistenta!\n', file_repo_inchirieri.modifica, inchiriere_noua)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere)
        self.assertTrue(lista_inchirieri[0].get_film() == film)
        self.assertTrue(lista_inchirieri[0].get_client() == client)
        self.assertTrue(lista_inchirieri[0].get_data() == data)
        self.assertTrue(len(lista_inchirieri) == 1)

        film_nou = Film(11, 'titlu nou', 'descriere noua', 'gen noua', 1979, 100)
        client_nou = Client(75, 'nume client', 3384294100230)
        data_noua = Data(9, 12, 2015)
        inchiriere_noua = Inchiriere(53, film_nou, client_nou, data_noua)

        file_repo_inchirieri.modifica(inchiriere_noua)

        lista_inchirieri = file_repo_inchirieri.get_all()
        self.assertTrue(file_repo_inchirieri.__len__() == 1)
        self.assertTrue(lista_inchirieri[0] == inchiriere_noua)
        self.assertTrue(len(lista_inchirieri) == 1)

        file.close()