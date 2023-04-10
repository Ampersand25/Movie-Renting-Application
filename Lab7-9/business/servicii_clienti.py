from domeniu.client_entitate import Client
from domeniu.inchiriere_entitate import Inchiriere

from erori.exceptii import ValidError

from random import *
import random
import string

class ServiceClienti:

    def __init__(self, validator_clienti, repo_clienti, repo_inchirieri):
        self.__validator_clienti = validator_clienti
        self.__repo_clienti = repo_clienti
        self.__repo_inchirieri = repo_inchirieri

    def __generare_numar_random(self, min, max):
        return randint(min, max + 1)

    def __generare_nume_random(self):
        lungime_nume = self.__generare_numar_random(3, 20)
        litere = string.ascii_lowercase
        nume = ''.join(random.choice(litere) for idx in range(lungime_nume))
        return nume

    def generare_clienti(self):
        nr_clienti = self.__generare_numar_random(5, 15)

        for idx in range(nr_clienti):
            id_client = self.__generare_numar_random(0, 1e+4)
            nume = self.__generare_nume_random()
            cnp = self.__generare_numar_random(1e+12, 1e+13 - 1)

            self.adauga_client(id_client, nume, cnp)

    def adauga_client(self, id_client, nume, cnp):
        client = Client(id_client, nume, cnp)
        self.__validator_clienti.valideaza(client)
        self.__repo_clienti.adauga(client)

    def get_clienti(self):
        return self.__repo_clienti.get_all()

    def sterge_client(self, id_client):
        if id_client < 0:
            raise ValidError('id client invalid!\n')

        inchirieri = self.__repo_inchirieri.get_all()

        for inchiriere in inchirieri:
            client = inchiriere.get_client()
            if id_client == client.get_id_client():
                id_inchiriere = inchiriere.get_id_inchiriere()
                self.__repo_inchirieri.sterge_dupa_id(id_inchiriere)

        self.__repo_clienti.sterge_dupa_id(id_client)

    def modifica_client(self, id_client, nume, cnp):
        client_nou = Client(id_client, nume, cnp)
        self.__validator_clienti.valideaza(client_nou)

        '''
        inchirieri = self.__repo_inchirieri.get_all()

        for inchiriere in inchirieri:
            client = inchiriere.get_client()
            if id_client == client.get_id_client():
                inchiriere_noua = Inchiriere(inchiriere.get_id_inchiriere(), inchiriere.get_film(), client_nou, inchiriere.get_data())
                self.__repo_inchirieri.modifica(inchiriere_noua)
        '''

        self.__repo_clienti.modifica(client_nou)

    def cauta_client(self, id_client):
        if id_client < 0 :
            raise ValidError('id client invalid!\n')

        return self.__repo_clienti.cauta_dupa_id(id_client)

    def nr_clienti(self):
        return len(self.__repo_clienti)