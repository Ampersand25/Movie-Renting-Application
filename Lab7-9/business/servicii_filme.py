from domeniu.film_entitate import Film
from domeniu.inchiriere_entitate import Inchiriere

from erori.exceptii import ValidError

from random import *
import random
import string

class ServiceFilme:

    def __init__(self, validator_filme, repo_filme, repo_inchirieri):
        self.__validator_filme = validator_filme
        self.__repo_filme = repo_filme
        self.__repo_inchirieri = repo_inchirieri

    def __generare_numar_random(self, min, max):
        return randint(min, max + 1)

    def __generare_nume_random(self):
        lungime_nume = self.__generare_numar_random(3, 20)
        litere = string.ascii_lowercase
        nume = ''.join(random.choice(litere) for idx in range(lungime_nume))
        return nume

    def generare_filme(self):
        nr_filme = self.__generare_numar_random(5, 15)

        for idx in range(nr_filme):
            id_film = self.__generare_numar_random(0, 1e+4)
            titlu = self.__generare_nume_random()
            descriere = self.__generare_nume_random()
            gen = self.__generare_nume_random()
            an_lansare = self.__generare_numar_random(1897, 2021)
            durata = self.__generare_numar_random(60, 210)

            self.adauga_film(id_film, titlu, descriere, gen, an_lansare, durata)

    def adauga_film(self, id_film, titlu, descriere, gen, an_lansare, durata):
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)
        self.__validator_filme.valideaza(film)
        self.__repo_filme.adauga(film)

    def get_filme(self):
        return self.__repo_filme.get_all()

    def sterge_film(self, id_film):
        if id_film < 0:
            raise ValidError('id film invalid!\n')

        inchirieri = self.__repo_inchirieri.get_all()

        for inchiriere in inchirieri:
            film = inchiriere.get_film()
            if id_film == film.get_id_film():
                id_inchiriere = inchiriere.get_id_inchiriere()
                self.__repo_inchirieri.sterge_dupa_id(id_inchiriere)

        self.__repo_filme.sterge_dupa_id(id_film)

    def modifica_flim(self, id_film, titlu, descriere, gen, an_lansare, durata):
        film_nou = Film(id_film, titlu, descriere, gen, an_lansare, durata)
        self.__validator_filme.valideaza(film_nou)

        '''
        inchirieri = self.__repo_inchirieri.get_all()

        for inchiriere in inchirieri:
            film = inchiriere.get_film()
            if id_film == film.get_id_film():
                inchiriere_noua = Inchiriere(inchiriere.get_id_inchiriere(), film_nou, inchiriere.get_client(), inchiriere.get_data())
                self.__repo_inchirieri.modifica(inchiriere_noua)
        '''

        self.__repo_filme.modifica(film_nou)

    def cauta_film(self, id_film):
        if id_film < 0:
            raise ValidError('id film invalid!\n')

        return self.__repo_filme.cauta_dupa_id(id_film)

    def nr_filme(self):
        return len(self.__repo_filme)