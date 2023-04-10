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
from erori.exceptii import RepoError

class RepositoryInchirieri:

    def __init__(self):
        self._inchirieri = []

    def adauga(self, inchiriere_noua):
        for inchiriere in self._inchirieri:
            if inchiriere == inchiriere_noua:
                raise RepoError('inchiriere deja existenta!\n')

        self._inchirieri.append(inchiriere_noua)

    def __len__(self):
        return len(self._inchirieri)

    def cauta_dupa_id(self, id_inchiriere):
        for inchiriere in self._inchirieri:
            if inchiriere.get_id_inchiriere() == id_inchiriere:
                return inchiriere

        raise RepoError('inchiriere inexistenta!\n')

    def get_all(self):
        return self._inchirieri[:]

    def modifica(self, inchiriere_noua):
        for idx in range(len(self._inchirieri)):
            if self._inchirieri[idx] == inchiriere_noua:
                '''
                self._inchirieri[idx] = inchiriere_noua
                '''

                self._inchirieri[idx].set_film(inchiriere_noua.get_film())
                self._inchirieri[idx].set_client(inchiriere_noua.get_client())
                self._inchirieri[idx].set_data(inchiriere_noua.get_data())
                return

        raise RepoError('inchiriere inexistenta!\n')

    def sterge_dupa_id(self, id_inchiriere):
        for idx in range(len(self._inchirieri)):
            if self._inchirieri[idx].get_id_inchiriere() == id_inchiriere:
                del self._inchirieri[idx]
                return

        raise RepoError('inchiriere inexistenta!\n')