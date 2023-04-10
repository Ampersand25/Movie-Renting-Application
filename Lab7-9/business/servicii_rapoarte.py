from utils.sortari import bingo_sort_func, merge_sort_func

class ServiceRapoarte:

    def __init__(self, repo_inchirieri):
        self.__repo_inchirieri = repo_inchirieri

    #raport 1
    def __func_clienti_inchirieri_iterativ(self, lista_clienti, lista_inchirieri):
        for inchiriere in lista_inchirieri:
            client = inchiriere.get_client()
            if client in lista_clienti:
                continue
            lista_clienti.append(client)
        return lista_clienti

    #-----------------------------------------------------------------------------
    #------------------------------FUNCTIE RECURSIVA------------------------------
    def __func_clienti_inchirieri_recursiv(self, lista_clienti, lista_inchirieri):
        #functie care returneaza o lista lista_clienti care contine toti clientii cu filme inchiriate din lista_inchirieri
        #base case
        if not len(lista_inchirieri):
            return lista_clienti
        #inductive step
        client = lista_inchirieri[0].get_client()
        if client not in lista_clienti:
            lista_clienti.append(client)
        return self.__func_clienti_inchirieri_recursiv(lista_clienti, lista_inchirieri[1:])

    def __clienti_inchirieri(self):
        lista_clienti = []
        #return self.__func_clienti_inchirieri_iterativ(lista_clienti, self.__repo_inchirieri.get_all())
        return self.__func_clienti_inchirieri_recursiv(lista_clienti, self.__repo_inchirieri.get_all())

    def __crescator_nume(self, client):
        return client.get_nume()

    @staticmethod
    def crescator_nume(client):
        return client.get_nume()

    def raport_clienti_1_ordonat_nume(self):
        lista_clienti = self.__clienti_inchirieri()
        #lista_clienti.sort(reverse=False, key=self.__crescator_nume)
        #bingo_sort_func(lista_clienti, key=ServiceRapoarte.crescator_nume, reverse=False, cmp=lambda x, y: x < y)
        merge_sort_func(lista_clienti, key=ServiceRapoarte.crescator_nume, reverse=False, cmp=lambda x, y: x < y)
        return lista_clienti

    def __cauta_client_lista_iterativ(self, lista_clienti_nrFilme, client):
        for idx in range(len(lista_clienti_nrFilme)):
            if lista_clienti_nrFilme[idx][0] == client:
                return idx
        return -1

    #---------------------------------------------------------------------------
    #-----------------------------FUNCTIE RECURSIVA-----------------------------
    def __cauta_client_lista_recursiv(self, lista_clienti_nrFilme, client, idx):
        #metoda I
        #base case
        if idx == len(lista_clienti_nrFilme):
            return -1
        #inductive step
        if lista_clienti_nrFilme[idx][0] == client:
            return idx
        return self.__cauta_client_lista_recursiv(lista_clienti_nrFilme, client, idx + 1)

        '''
        #metoda II
        #base case
        if not len(lista_clienti_nrFilme):
            return -1
        #inductive step
        if lista_clienti_nrFilme[0][0] == client:
            return idx
        return self.__cauta_client_lista_recursiv(lista_clienti_nrFilme[1:], client, idx + 1)
        '''

    def __clienti_inchirieri_nr_filme(self):
        lista_clienti_nrFilme = []
        lista_inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in lista_inchirieri:
            client = inchiriere.get_client()
            pos = self.__cauta_client_lista_iterativ(lista_clienti_nrFilme, client)
            #pos = self.__cauta_client_lista_recursiv(lista_clienti_nrFilme, client, 0)
            if pos != -1:
                lista_clienti_nrFilme[pos][1] += 1
            else:
                lista_clienti_nrFilme.append([client, 1])
        return lista_clienti_nrFilme

    def __nr_filme(self, pereche_client_nrFilme):
        return pereche_client_nrFilme[1]

    @staticmethod
    def get_nr_filme(pereche_client_nrFilme):
        return pereche_client_nrFilme[1]

    @staticmethod
    def crescator_nr_filme_nume(pereche_client_nrFilme):
        return pereche_client_nrFilme[1], pereche_client_nrFilme[0].get_nume()

    @staticmethod
    def cmp_func(pereche_client_nrFilme1, pereche_client_nrFilme2):
        if pereche_client_nrFilme1[1] == pereche_client_nrFilme2[1]:
            return pereche_client_nrFilme1[0].get_nume() >= pereche_client_nrFilme2[0].get_nume()
        return pereche_client_nrFilme1[1] < pereche_client_nrFilme2[1]

    def raport_clienti_1_ordonat_nr_filme(self):
        lista_clienti_nrFilme = self.__clienti_inchirieri_nr_filme()
        #lista_clienti_nrFilme.sort(reverse=False, key=self.__nr_filme)

        bingo_sort_func(lista_clienti_nrFilme, key=ServiceRapoarte.get_nr_filme, reverse=False, cmp=lambda x, y: x < y)
        #bingo_sort_func(lista_clienti_nrFilme, key=ServiceRapoarte.crescator_nr_filme_nume, reverse=False, cmp=lambda x, y: x < y)
        #bingo_sort_func(lista_clienti_nrFilme, reverse=False, cmp=ServiceRapoarte.cmp_func)

        #merge_sort_func(lista_clienti_nrFilme, reverse=False, cmp=ServiceRapoarte.cmp_func)
        return lista_clienti_nrFilme

    #raport 2
    def __cauta_film_lista_iterativ(self, lista_filme_nrInchirieri, film):
        for idx in range(len(lista_filme_nrInchirieri)):
            if lista_filme_nrInchirieri[idx][0] == film:
                return idx
        return -1

    #--------------------------------------------------------------------------
    #-----------------------------FUNCTIE RECURSIVA----------------------------
    def __cauta_film_lista_recursiv(self, lista_filme_nrInchirieri, film, idx):
        #metoda I
        #base case
        if idx == len(lista_filme_nrInchirieri):
            return -1
        #inductive step
        if lista_filme_nrInchirieri[idx][0] == film:
            return idx
        return self.__cauta_film_lista_recursiv(lista_filme_nrInchirieri, film, idx + 1)

        '''
        #metoda II
        #base case
        if not len(lista_filme_nrInchirieri):
            return -1
        #inductive step
        if lista_filme_nrInchirieri[0][0] == film:
            return idx
        return self.__cauta_film_lista_recursiv(lista_filme_nrInchirieri[1:], film, idx + 1)
        '''

    def __filme_inchirieri_nr_inchirieri(self):
        lista_filme_nrInchirieri = []
        lista_inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in lista_inchirieri:
            film = inchiriere.get_film()
            #pos = self.__cauta_film_lista_iterativ(lista_filme_nrInchirieri, film)
            pos = self.__cauta_film_lista_recursiv(lista_filme_nrInchirieri, film, 0)
            if pos != -1:
                lista_filme_nrInchirieri[pos][1] += 1
            else:
                lista_filme_nrInchirieri.append([film, 1])
        return lista_filme_nrInchirieri

    def __nr_inchirieri(self, pereche_film_nrInchirieri):
        return pereche_film_nrInchirieri[1]

    @staticmethod
    def get_nr_inchirieri(pereche_film_nrInchirieri):
        return pereche_film_nrInchirieri[1]

    def raport_filme(self):
        lista_filme_nrInchirieri = self.__filme_inchirieri_nr_inchirieri()
        #lista_filme_nrInchirieri.sort(reverse = True, key = self.__nr_inchirieri)
        #bingo_sort_func(lista_filme_nrInchirieri, key=ServiceRapoarte.get_nr_inchirieri, reverse=True, cmp=lambda x, y: x < y)
        merge_sort_func(lista_filme_nrInchirieri, key=ServiceRapoarte.get_nr_inchirieri, reverse=True, cmp=lambda x, y: x < y)
        return lista_filme_nrInchirieri

    #raport 3
    @staticmethod
    def get_nr_filme(pereche_client_nrFilme):
        return pereche_client_nrFilme[1]

    def raport_clienti_2(self):
        lista_clienti_nrFilme = self.__clienti_inchirieri_nr_filme()
        #lista_clienti_nrFilme.sort(reverse = True, key = self.__nr_filme)
        #bingo_sort_func(lista_clienti_nrFilme, key=ServiceRapoarte.get_nr_filme, reverse=True, cmp=lambda x, y: x < y)
        merge_sort_func(lista_clienti_nrFilme, key=ServiceRapoarte.get_nr_filme, reverse=True, cmp=lambda x, y: x < y)
        return lista_clienti_nrFilme

    #raport 4
    def __func_filme_inchiriate_iterativ(self, lista_filme_inchiriate, lista_inchirieri):
        for inchiriere in lista_inchirieri:
            film = inchiriere.get_film()
            if film in lista_filme_inchiriate:
                continue
            else:
                lista_filme_inchiriate.append(film)
        return lista_filme_inchiriate

    #------------------------------------------------------------------------------------
    #---------------------------------FUNCTIE RECURSIVA----------------------------------
    def __func_filme_inchiriate_recursiv(self, lista_filme_inchiriate, lista_inchirieri):
        #base case
        if not len(lista_inchirieri):
            return lista_filme_inchiriate
        #inductive step
        film = lista_inchirieri[0].get_film()
        if film not in lista_filme_inchiriate:
            lista_filme_inchiriate.append(film)
        return self.__func_filme_inchiriate_recursiv(lista_filme_inchiriate, lista_inchirieri[1:])

    def __filme_inchiriate(self):
        lista_filme_inchiriate = []
        #return self.__func_filme_inchiriate_iterativ(lista_filme_inchiriate, self.__repo_inchirieri.get_all())
        return self.__func_filme_inchiriate_recursiv(lista_filme_inchiriate, self.__repo_inchirieri.get_all())

    def raport_filme_2(self):
        lista_filme_inchiriate = self.__filme_inchiriate()
        return lista_filme_inchiriate