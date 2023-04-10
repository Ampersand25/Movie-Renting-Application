import unittest

from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
from domeniu.data_entitate import Data
from domeniu.inchiriere_entitate import Inchiriere

class TestCaseFilmDomeniu(unittest.TestCase):

    def testFilm1(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        self.assertEqual(film.get_id_film(), id_film)
        self.assertEqual(film.get_titlu(), titlu)
        self.assertEqual(film.get_descriere(), descriere)
        self.assertEqual(film.get_gen(), gen)
        self.assertEqual(film.get_an_lansare(), an_lansare)
        self.assertEqual(film.get_durata(), durata)
        self.assertEqual(str(film), 'id: 21\ntitlu: I Am Mother\ndescriere: We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.\ngen: sci-fi\nan lansare: 2019\ndurata totala (minute): 113\n')

    def testFilm2(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)
        self.assertEqual(film.get_titlu(), titlu_nou)
        self.assertEqual(str(film), 'id: 21\ntitlu: IT\ndescriere: We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.\ngen: sci-fi\nan lansare: 2019\ndurata totala (minute): 113\n')

    def testFilm3(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)
        self.assertEqual(film.get_descriere(), descriere_noua)
        self.assertEqual(str(film), 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: sci-fi\nan lansare: 2019\ndurata totala (minute): 113\n')

    def testFilm4(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)

        gen_nou = 'horror'
        film.set_gen(gen_nou)
        self.assertEqual(film.get_gen(), gen_nou)
        self.assertEqual(str(film), 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: horror\nan lansare: 2019\ndurata totala (minute): 113\n')

    def testFilm5(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)

        gen_nou = 'horror'
        film.set_gen(gen_nou)

        an_lansare_nou = 2017
        film.set_an_lansare(an_lansare_nou)
        self.assertEqual(film.get_an_lansare(), an_lansare_nou)
        self.assertEqual(str(film), 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: horror\nan lansare: 2017\ndurata totala (minute): 113\n')

    def testFilm6(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)

        gen_nou = 'horror'
        film.set_gen(gen_nou)

        an_lansare_nou = 2017
        film.set_an_lansare(an_lansare_nou)

        durata_noua = 135
        film.set_durata(durata_noua)
        self.assertEqual(film.get_durata(), durata_noua)
        self.assertEqual(str(film), 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: horror\nan lansare: 2017\ndurata totala (minute): 135\n')

    def testFilm7(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)

        gen_nou = 'horror'
        film.set_gen(gen_nou)

        an_lansare_nou = 2017
        film.set_an_lansare(an_lansare_nou)

        durata_noua = 135
        film.set_durata(durata_noua)

        alt_film = Film(id_film, '', '', '', 0, 0)

        self.assertEqual(film, alt_film)

        self.assertEqual(film.__eq__(alt_film), True)
        self.assertEqual(True, film.__eq__(alt_film))
        self.assertTrue(film.__eq__(alt_film))

        self.assertEqual(id(film) != id(alt_film), True)
        self.assertEqual(True, id(film) != id(alt_film))
        self.assertTrue(id(film) != id(alt_film))

    def testFilm8(self):
        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)

        gen_nou = 'horror'
        film.set_gen(gen_nou)

        an_lansare_nou = 2017
        film.set_an_lansare(an_lansare_nou)

        durata_noua = 135
        film.set_durata(durata_noua)

        alt_film = Film(id_film + 1, '', '', '', 0, 0)

        self.assertTrue(film != alt_film)
        self.assertTrue(not film.__eq__(alt_film))
        self.assertTrue(id(film) != id(alt_film))

class TestCaseClientDomeniu(unittest.TestCase):

    def testClient1(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        self.assertEqual(client.get_id_client(), id_client)
        self.assertEqual(client.get_nume(), nume)
        self.assertEqual(client.get_cnp(), cnp)
        self.assertEqual(str(client), 'id: 35\nnume: Popescu Mihai\ncnp: 1951124682471\n')

    def testClient2(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        self.assertEqual(client.get_id_client(), id_client)
        self.assertEqual(client.get_nume(), nume_nou)
        self.assertEqual(client.get_cnp(), cnp)
        self.assertEqual(str(client), 'id: 35\nnume: Ionescu Alexandru\ncnp: 1951124682471\n')

    def testClient3(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        cnp_nou = 8523396531853
        client.set_cnp(cnp_nou)

        self.assertEqual(client.get_id_client(), id_client)
        self.assertEqual(client.get_nume(), nume_nou)
        self.assertEqual(client.get_cnp(), cnp_nou)
        self.assertEqual(str(client), 'id: 35\nnume: Ionescu Alexandru\ncnp: 8523396531853\n')

        cnp = cnp_nou

    def testClient4(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        cnp_nou = 8523396531853
        client.set_cnp(cnp_nou)
        cnp = cnp_nou

        alt_client = Client(id_client, '', cnp - 1)

        self.assertEqual(client, alt_client)
        self.assertTrue(client.__eq__(alt_client))
        self.assertTrue(id(client) != id(alt_client))

    def testClient5(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        cnp_nou = 8523396531853
        client.set_cnp(cnp_nou)
        cnp = cnp_nou

        alt_client = Client(id_client + 1, '', cnp)

        self.assertEqual(client, alt_client)
        self.assertTrue(client.__eq__(alt_client))
        self.assertTrue(id(client) != id(alt_client))

    def testClient6(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        cnp_nou = 8523396531853
        client.set_cnp(cnp_nou)
        cnp = cnp_nou

        alt_client = Client(id_client, '', cnp)

        self.assertEqual(client, alt_client)
        self.assertTrue(client.__eq__(alt_client))
        self.assertTrue(id(client) != id(alt_client))

    def testClient7(self):
        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        cnp_nou = 8523396531853
        client.set_cnp(cnp_nou)
        cnp = cnp_nou

        alt_client = Client(id_client - 1, '', cnp + 1)

        self.assertTrue(client != alt_client)
        self.assertTrue(not client.__eq__(alt_client))
        self.assertTrue(id(client) != id(alt_client))

class TestCaseDataDomeniu(unittest.TestCase):

    def testData1(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        self.assertEqual(data.get_zi(), zi)
        self.assertEqual(data.get_luna(), luna)
        self.assertEqual(data.get_an(), an)
        self.assertEqual(str(data), '14.03.2023\n')

    def testData2(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        self.assertEqual(data.get_zi(), zi_noua)
        self.assertEqual(data.get_luna(), luna)
        self.assertEqual(data.get_an(), an)
        self.assertEqual(str(data), '9.03.2023\n')

    def testData3(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        self.assertEqual(data.get_zi(), zi_noua)
        self.assertEqual(data.get_luna(), luna_noua)
        self.assertEqual(data.get_an(), an)
        self.assertEqual(str(data), '9.11.2023\n')

    def testData4(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        self.assertEqual(data.get_zi(), zi_noua)
        self.assertEqual(data.get_luna(), luna_noua)
        self.assertEqual(data.get_an(), an_nou)
        self.assertEqual(str(data), '9.11.1963\n')

    def testData5(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua, luna_noua, an_nou)
        self.assertTrue(data == data_noua)

    def testData6(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua - 1, luna_noua, an_nou)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua + 1, luna_noua, an_nou)
        self.assertTrue(data != data_noua)

    def testData7(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua, luna_noua - 1, an_nou)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua, luna_noua + 1, an_nou)
        self.assertTrue(data != data_noua)

    def testData8(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua, luna_noua, an_nou - 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua, luna_noua, an_nou + 1)
        self.assertTrue(data != data_noua)

    def testData9(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua - 1, luna_noua - 1, an_nou)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua - 1, luna_noua + 1, an_nou)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua + 1, luna_noua - 1, an_nou)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua + 1, luna_noua + 1, an_nou)
        self.assertTrue(data != data_noua)

    def testData10(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua - 1, luna_noua, an_nou - 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua - 1, luna_noua, an_nou + 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua + 1, luna_noua, an_nou - 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua + 1, luna_noua, an_nou + 1)
        self.assertTrue(data != data_noua)

    def testData11(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua, luna_noua - 1, an_nou - 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua, luna_noua - 1, an_nou + 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua, luna_noua + 1, an_nou - 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua, luna_noua + 1, an_nou + 1)
        self.assertTrue(data != data_noua)

    def testData12(self):
        zi = 14
        luna = 3
        an = 2023
        data = Data(zi, luna, an)

        zi_noua = 9
        data.set_zi(zi_noua)

        luna_noua = 11
        data.set_luna(luna_noua)

        an_nou = 1963
        data.set_an(an_nou)

        data_noua = Data(zi_noua - 1, luna_noua - 1, an_nou - 1)
        self.assertTrue(data != data_noua)

        data_noua = Data(zi_noua + 1, luna_noua + 1, an_nou + 1)
        self.assertTrue(data != data_noua)

class TestCaseInchiriereDomeniu(unittest.TestCase):

    def testInchiriere1(self):
        id_inchiriere = 13

        id_film = 8
        titlu = 'The Godfather'
        descriere = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
        gen = 'crima si drama'
        an_lansare = 1972
        durata = 175
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        id_client = 0
        nume = 'Dragos Stefan Spiridon'
        cnp = 8527138653283
        client = Client(id_client, nume, cnp)

        zi = 21
        luna = 12
        an = 2007
        data = Data(zi, luna, an)

        inchiriere = Inchiriere(id_inchiriere, film, client, data)

        self.assertEqual(inchiriere.get_id_inchiriere(), id_inchiriere)
        self.assertEqual(inchiriere.get_film(), film)
        self.assertEqual(inchiriere.get_client(), client)
        self.assertEqual(inchiriere.get_data(), data)

    def testInchiriere2(self):
        id_inchiriere = 13

        id_film = 8
        titlu = 'The Godfather'
        descriere = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
        gen = 'crima si drama'
        an_lansare = 1972
        durata = 175
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        id_client = 0
        nume = 'Dragos Stefan Spiridon'
        cnp = 8527138653283
        client = Client(id_client, nume, cnp)

        zi = 21
        luna = 12
        an = 2007
        data = Data(zi, luna, an)

        inchiriere = Inchiriere(id_inchiriere, film, client, data)

        film_nou = Film(3, 'titlu', 'descriere', 'gen', 1986, 78)
        inchiriere.set_film(film_nou)

        self.assertEqual(inchiriere.get_id_inchiriere(), id_inchiriere)
        self.assertEqual(inchiriere.get_film(), film_nou)
        self.assertEqual(inchiriere.get_client(), client)
        self.assertEqual(inchiriere.get_data(), data)

    def testInchiriere3(self):
        id_inchiriere = 13

        id_film = 8
        titlu = 'The Godfather'
        descriere = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
        gen = 'crima si drama'
        an_lansare = 1972
        durata = 175
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        id_client = 0
        nume = 'Dragos Stefan Spiridon'
        cnp = 8527138653283
        client = Client(id_client, nume, cnp)

        zi = 21
        luna = 12
        an = 2007
        data = Data(zi, luna, an)

        inchiriere = Inchiriere(id_inchiriere, film, client, data)

        client_nou = Client(63, 'nume', 4444444444444)
        inchiriere.set_client(client_nou)

        self.assertEqual(inchiriere.get_id_inchiriere(), id_inchiriere)
        self.assertEqual(inchiriere.get_film(), film)
        self.assertEqual(inchiriere.get_client(), client_nou)
        self.assertEqual(inchiriere.get_data(), data)

    def testInchiriere4(self):
        id_inchiriere = 13

        id_film = 8
        titlu = 'The Godfather'
        descriere = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
        gen = 'crima si drama'
        an_lansare = 1972
        durata = 175
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        id_client = 0
        nume = 'Dragos Stefan Spiridon'
        cnp = 8527138653283
        client = Client(id_client, nume, cnp)

        zi = 21
        luna = 12
        an = 2007
        data = Data(zi, luna, an)

        inchiriere = Inchiriere(id_inchiriere, film, client, data)

        data_noua = Data(17, 1, 1999)
        inchiriere.set_data(data_noua)

        self.assertEqual(inchiriere.get_id_inchiriere(), id_inchiriere)
        self.assertEqual(inchiriere.get_film(), film)
        self.assertEqual(inchiriere.get_client(), client)
        self.assertEqual(inchiriere.get_data(), data_noua)

    def testInchiriere5(self):
        id_inchiriere = 13

        id_film = 8
        titlu = 'The Godfather'
        descriere = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
        gen = 'crima si drama'
        an_lansare = 1972
        durata = 175
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        id_client = 0
        nume = 'Dragos Stefan Spiridon'
        cnp = 8527138653283
        client = Client(id_client, nume, cnp)

        zi = 21
        luna = 12
        an = 2007
        data = Data(zi, luna, an)

        inchiriere = Inchiriere(id_inchiriere, film, client, data)

        inchiriere_noua = Inchiriere(id_inchiriere, film, client, data)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        film_nou = Film(3, 'titlu', 'descriere', 'gen', 1986, 78)

        inchiriere_noua = Inchiriere(id_inchiriere, film_nou, client, data)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        client_nou = Client(63, 'nume', 4444444444444)

        inchiriere_noua = Inchiriere(id_inchiriere, film, client_nou, data)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        data_noua = Data(17, 1, 1999)

        inchiriere_noua = Inchiriere(id_inchiriere, film, client, data_noua)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        inchiriere_noua = Inchiriere(id_inchiriere, film_nou, client_nou, data)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        inchiriere_noua = Inchiriere(id_inchiriere, film_nou, client, data_noua)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        inchiriere_noua = Inchiriere(id_inchiriere, film, client_nou, data_noua)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

        inchiriere_noua = Inchiriere(id_inchiriere, film_nou, client_nou, data_noua)
        self.assertTrue(inchiriere.__eq__(inchiriere_noua))

    def testInchiriere6(self):
        id_inchiriere = 13

        id_film = 8
        titlu = 'The Godfather'
        descriere = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
        gen = 'crima si drama'
        an_lansare = 1972
        durata = 175
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        id_client = 0
        nume = 'Dragos Stefan Spiridon'
        cnp = 8527138653283
        client = Client(id_client, nume, cnp)

        zi = 21
        luna = 12
        an = 2007
        data = Data(zi, luna, an)

        inchiriere = Inchiriere(id_inchiriere, film, client, data)

        str_inchiriere = 'id inchiriere: ' + str(id_inchiriere) + '\n\nclient:\n' + str(client) + '\nfilm:\n' + str(film) + '\ntermen returnare film:\n' + str(data) + '\n'
        self.assertTrue(str_inchiriere == str(inchiriere))
        self.assertEqual(str(inchiriere), str_inchiriere)

        inchiriere_noua = Inchiriere(id_inchiriere - 1, film, client, data)
        self.assertTrue(inchiriere != inchiriere_noua)

        inchiriere_noua = Inchiriere(id_inchiriere + 1, film, client, data)
        self.assertTrue(inchiriere != inchiriere_noua)