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

class RepositoryFilme:
    #pentru fiecare din cele 7 operatii permise pe un repository ne definim cate o metoda la nivelul clasei repository-ului

    #operatie care creeaza un repository nou de filme (un nou obiect de clasa RepositoryFilme)
    def __init__(self):
        #constructor (functie/metoda) care initializeaza lista de filme (camp/componenta a clasei RepositoryFilme) din repository cu o lista vida la crearea unui nou repository
        #date de intrare: -
        #date de iesire: -

        self._filme = [] #initial repository-ul de filme este gol (reprezentat ca si o lista vida)

    #operatie de tipul C (Create), care adauga o noua carte la un repository de carti (asta daca cartea respectiva nu exista deja in repo <=> nu exista alta carte care sa aiba acelasi id ca si cartea pe care vrem sa o salvam in repo)
    #aceasta operatie poate modifica marimea repository-ului (adica poate sa creasca cu 1 numarul de filme din repository <=> creste lungimea listei de filme din repo)
    def adauga(self, film_nou):
        #metoda care incearca sa adauge un nou film film_nou la repository-ul de filme
        #date de intrare: film_nou - obiect de clasa Film pe care vrem sa il adaugam in repo
        #date de iesire: -, daca adaugarea s-a efectuat cu succes (nu s-a gasit un film existent in repository care sa aiba acelasi id cu filmul film_nou)
        #                eroare de tipul RepoError cu mesajul 'film deja existent!\n', in caz contrar (nu s-a adaugat filmul film_nou la lista de filme din repository)

        for film in self._filme:
            if film == film_nou:
                raise RepoError('film deja existent!\n')

        self._filme.append(film_nou)

    #operatii de tipul R (Read), care nu modifica lista de filme din repo, doar returneaza o informatie referitoare la starea acesteia accesand-o
    def __len__(self):
        #metoda care furnizeaza numarul de filme din repository
        #date de intrare: -
        #date de iesire: intreg - numarul de filme din repo (adica lungimea listei de filme din clasa RepositoryFilme)

        return len(self._filme)

    def cauta_dupa_id(self, id_film):
        #metoda care cauta un film in repository dupa id-ul acestuia si returneaza filmul cu id-ul id_film din repo daca acesta exista sau o eroare definita de programator in caz opus
        #date de intrare: id_film - intreg (fara semn) care reprezinta identificatorul unic al filmului pe care il cautam in repo
        #date de iesire: obiect de clasa Film - daca s-a gasit un film cu id-ul id_film in lista de filme din repository
        #                eroare de tipul RepoError cu mesajul 'film inexistent!\n' - in cazul in care niciunul dintre filmele existente in repo nu au id-ul id_film

        for film in self._filme:
            if film.get_id_film() == id_film:
                return film

        raise RepoError('film inexistent!\n')

    def get_all(self):
        #metoda care ne returneaza lista tuturor filmelor din repo
        #date de intrare: -
        #date de iesire: lista de obiecte de clasa Film - o copie shallow a listei de filme din campul/componenta privata filme a obiectului de clasa RepositoryFilme

        return self._filme[:]

    #operatie de tipul U (Update), care modifica lista de filme de la nivelul repository-ului prin inlocuirea unui film din repository (daca si numai daca filmul respectiv se alfa in lista de filme din repo) cu un altul care trebuie sa aiba acelasi id ca si filmul pe care dorim sa il inlocuim (astfel se pastreaza id-ul filmului initial si se modifica doar celelalte campuri)
    #aceasta operatie nu afecteaza lungimea repository-ului (adica a numarului de filme din el)
    def modifica(self, film_nou):
        #metoda/functie care cauta in repository un obiect de clasa Film cu acelasi id ca si film_nou si daca il gaseste atunci il inlocuieste cu obiectul de clasa Film, film_nou
        #date de intrare: film_nou - obiect de clasa Film
        #date de iesire: -, daca s-a gasit un film cu acelasi id ca si filmul film_nou
        #                exceptie de tipul RepoError cu mesajul de eroare 'film inexistent!\n', in caz contrar

        for idx in range(len(self._filme)):
            if self._filme[idx] == film_nou:
                ''''
                self._filme[idx] = film_nou
                '''

                self._filme[idx].set_titlu(film_nou.get_titlu())
                self._filme[idx].set_descriere(film_nou.get_descriere())
                self._filme[idx].set_gen(film_nou.get_gen())
                self._filme[idx].set_an_lansare(film_nou.get_an_lansare())
                self._filme[idx].set_durata(film_nou.get_durata())
                return

        raise RepoError('film inexistent!\n')

    #operatie de tipul D (Delete), care modifica lista de filme prin eliminarea (stergerea) unui element din lista de filme din repository (asta daca filmul respectiv se afla/gaseste in repo)
    #aceasta operatie poate modifica dimensiunea repository-ului spre deosebire de operatia de modificare (adica poate sa scada cu 1 numarul de filme din repository spre deosebire de operatia adauga din R unde acest numar crestea cu 1)
    def sterge_dupa_id(self, id_film):
        #metoda/functie care cauta un film in repositoy care sa aiba id-ul id_film si daca il gaseste, atunci il elimina (sterge) din lista de filme din repository
        #date de intrare: id_film - intreg care reprezinta id-ul filmului pe care dorim sa il stergem din repo
        #date de iesire: -, daca filmul cu id-ul id_film a fost gasit si implicit sters din repository
        #                exceptie de tipul RepoError cu mesajul de eroare 'film inexistent!\n' in caz contrar

        for idx in range(len(self._filme)):
            if self._filme[idx].get_id_film() == id_film:
                del self._filme[idx]
                return

        raise RepoError('film inexistent!\n')