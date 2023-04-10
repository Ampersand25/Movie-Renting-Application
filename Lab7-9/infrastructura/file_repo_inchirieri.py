#definim doua clase pentru fiecare din repository-urile programului, una pentru repository-ul de filme, iar cealalta pentru repository-ul de clienti
#fiecarei entitati (filme si clienti) din aplicatia noastra ii corespunde un repository (o lista de entitati de acelasi fel ca si entitatea aleasa)
#pe un repository avem definite urmatoarele 7 operatii fundamentale (implementate la nivel de funtii/metode in clasa repository-ului):
#(1) __init__ (initializeaza toate campurile/componentele din repository, este vorba despre lista de elemente care va fi initializata cu o lista vida)
#C - Create: (2) adauga(element) (adauga un nou element la repository, respectiv in lista de elemente)
#R - Read:   (3) cauta(id) -> element (trebuie ca element.get_id(element) == id) (cauta un element in repository dupa un id dat, se va face o cautare pe lista de elemente din repo)
#            (4) size()    -> intreg fara semn (numarul elementelor din repository) (returneaza lungimea fizica a repository-ului, adica lungimea listei de elemente din repo care corespunde numarului de elemente din repository)
#            (5) get_all() -> lista tutoror elementelor din repo (returneaza lista tuturor elementelor din repositoy de la un moment dat, se va returna o copie shallow a listei de elemente stocata ca si camp/componenta in clasa repo-ului, copie shallow: nu se copiaza adresa listei initiale, ci doar continutul acesteia)
#U - Update: (6) modifica(element) (modifica un element deja existent in repo)
#D - Delete: (7) sterge(element) (sterge/elimina un element din repository, daca acesta exista, daca nu se returneaza o eroare de tipul RepoError, adica Exception)

#din pachetul erori, modulul (fisierul py) exceptii, importam clasa RepoError cu care vom semnala erorile de la nivelul claselor RepositoryFilme si respectiv RepositoryClienti
from infrastructura.repo_inchirieri import RepositoryInchirieri
from domeniu.inchiriere_entitate import Inchiriere
from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
from domeniu.data_entitate import Data

class FileRepositoryInchirieri(RepositoryInchirieri):

    def __init__(self, filename):
        self.__filename = filename
        RepositoryInchirieri.__init__(self)

    def __citeste_tot_din_fisier(self):
        with open(self.__filename, 'r') as f:
            self._inchirieri = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    parts = line.split(';')
                    parts_film = parts[1].split(',')
                    film = Film(int(parts_film[0]), parts_film[1], parts_film[2], parts_film[3], int(parts_film[4]), int(parts_film[5]))
                    parts_client = parts[2].split(',')
                    client = Client(int(parts_client[0]), parts_client[1], int(parts_client[2]))
                    parts_data = parts[3].split('.')
                    data = Data(int(parts_data[0]), int(parts_data[1]), int(parts_data[2]))
                    inchiriere = Inchiriere(int(parts[0]), film, client, data)
                    self._inchirieri.append(inchiriere)

    def __append_inchiriere_fisier(self, inchiriere_noua):
        with open(self.__filename, 'a') as f:
            film = inchiriere_noua.get_film()
            client = inchiriere_noua.get_client()
            data = inchiriere_noua.get_data()
            f.write(str(inchiriere_noua.get_id_inchiriere()) + ';' + str(film.get_id_film()) + ',' + film.get_titlu() + ',' + film.get_descriere() + ',' + film.get_gen() + ',' + str(film.get_an_lansare()) + ',' + str(film.get_durata()) + ';' + str(client.get_id_client()) + ',' + client.get_nume() + ',' + str(client.get_cnp()) + ';' + str(data.get_zi()) + '.' + str(data.get_luna()) + '.' + str(data.get_an()) + '\n')

    def __scrie_tot_in_fisier(self):
        with open(self.__filename, 'w') as f:
            for inchiriere in self._inchirieri:
                film = inchiriere.get_film()
                client = inchiriere.get_client()
                data = inchiriere.get_data()
                f.write(str(inchiriere.get_id_inchiriere()) + ';' + str(film.get_id_film()) + ',' + film.get_titlu() + ',' + film.get_descriere() + ',' + film.get_gen() + ',' + str(film.get_an_lansare()) + ',' + str(film.get_durata()) + ';' + str(client.get_id_client()) + ',' + client.get_nume() + ',' + str(client.get_cnp()) + ';' + str(data.get_zi()) + '.' + str(data.get_luna()) + '.' + str(data.get_an()) + '\n')

    def adauga(self, inchiriere_noua):
        self.__citeste_tot_din_fisier()
        RepositoryInchirieri.adauga(self, inchiriere_noua)
        self.__append_inchiriere_fisier(inchiriere_noua)

    def __len__(self):
        self.__citeste_tot_din_fisier()
        return RepositoryInchirieri.__len__(self)

    def cauta_dupa_id(self, _id_inchiriere):
        self.__citeste_tot_din_fisier()
        return RepositoryInchirieri.cauta_dupa_id(self, _id_inchiriere)

    def get_all(self):
        self.__citeste_tot_din_fisier()
        return RepositoryInchirieri.get_all(self)

    def modifica(self, inchiriere_noua):
        self.__citeste_tot_din_fisier()
        RepositoryInchirieri.modifica(self, inchiriere_noua)
        self.__scrie_tot_in_fisier()

    def sterge_dupa_id(self, _id_inchiriere):
        self.__citeste_tot_din_fisier()
        RepositoryInchirieri.sterge_dupa_id(self, _id_inchiriere)
        self.__scrie_tot_in_fisier()