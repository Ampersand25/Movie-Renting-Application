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

class RepositoryClienti:
    #pentru fiecare din cele 7 operatii permise pe un repository ne definim cate o metoda la nivelul clasei repository-ului

    #operatie care creeaza un repository nou de clienti (un nou obiect de clasa RepositoryClienti)
    def __init__(self):
        #constructor (functie/metoda) care initializeaza lista de clienti (camp/componenta a clasei RepositoryClienti) din repository cu o lista vida la crearea unui nou repository
        #date de intrare: - (nimic)
        #date de iesire: - (nimic)

        self._clienti = [] #initial repository-ul de clienti este gol (reprezentat ca si o lista vida)

    #operatie de tipul C (Create), care adauga un nou client la un repository de clienti (asta daca clientul respectiv nu exista deja in repo <=> nu exista alt client cu acelasi id ca si clientul pe care dorim sa il adaugam in repo)
    #aceasta operatie poate modifica dimensiunea repository-ului (adica se poate face incrementul cu 1 a numarului de clienti din repository <=> se modifica lungimea listei de clienti)
    def adauga(self, client_nou):
        #metoda care incearca sa adauge un nou client client_nou (obiect de clasa Client) la repository-ul de clienti (adica in lista de clienti din clasa RepositoryClienti)
        #date de intrare: client_nou - obiect de clasa Client pe care vrem sa il adaugam in repo
        #date de iesire: -, daca adaugarea s-a efectuat cu succes (nu s-a gasit un client deja existent in repository care sa aiba acelasi id cu clientul client_nou sau acelasi cnp)
        #               eroare de tipul RepoError cu mesajul 'client deja existent!\n', in caz contrar (nu s-a adaugat clientul client_nou la lista de clienti din cadrul repository-ului, acesta existand deja in repo)

        for client in self._clienti:
            if client == client_nou:
                raise RepoError('client deja existent!\n')

        self._clienti.append(client_nou)

    #operatii de tipul R (Read), care nu modifica lista de clienti din repo, doar returneaza o informatie referitoare la starea acesteia accesand-o
    def __len__(self):
        #metoda care furnizeaza numarul de clienti din lista de clienti din repository
        #date de intrare: -
        #date de iesire: intreg - numarul de clienti din repo (adica lungimea campului/componentei private clienti de tip lista a unui obiect de clasa RepositoryClienti)

        return len(self._clienti)

    def cauta_dupa_id(self, id_client):
        #metoda care cauta un client in repository dupa id-ul acestuia si returneaza clientul cu id-ul id_client din repo daca acesta exista sau o eroare definita de programator in caz contrar
        #date de intrare: id_client - intreg (unsigned) care reprezinta identificatorul unic al clientului pe care il cautam in lista de clienti clienti din repo
        #date de iesire: obiect de clasa Client - daca s-a gasit un client cu id-ul id_client in lista de clienti din repository
        #                eroare de tipul RepoError cu mesajul 'client inexistent!\n' - in cazul in care niciunul dintre clientii existenti in repo nu au id-ul id_client

        for client in self._clienti:
            if client.get_id_client() == id_client:
                return client

        raise RepoError('client inexistent!\n')

    def get_all(self):
        #metoda care ne returneaza lista tuturor clientilor din repo
        #date de intrare: -
        #date de iesire: lista de obiecte de clasa Client - o copie shallow a listei de clienti din campul/componenta privata clienti a obiectului de clasa RepositoryClienti

        return self._clienti[:]

    #operatie de tipul U (Update), care modifica lista de clienti de la nivelul repository-ului prin inlocuirea unui client din repository (daca si numai daca clientul respectiv se alfa in lista de clienti din repo) cu un altul care trebuie sa aiba acelasi id sau cnp ca si clientul pe care dorim sa il inlocuim (astfel se pastreaza id-ul si cnp-ul clientului initial)
    #aceasta operatie nu afecteaza dimensiunea repository-ului (adica a numarului de clienti stocati in interiorul sau, lungimea listei de clienti ramane aceeasi in urma operatiei)
    def modifica(self, client_nou):
        #metoda/functie care cauta in repository un obiect de clasa Client cu acelasi id sau cnp ca si client_nou si daca gaseste un astfel de obiect de clasa Client, atunci il inlocuieste cu clientul client_nou
        #date de intrare: client_nou - obiect de clasa Client
        #date de iesire: -, daca s-a gasit un client cu acelasi id sau cnp ca si clientul client_nou
        #               exceptie de tipul RepoError cu mesajul de eroare 'client inexistent!\n', in caz contrar

        for idx in range(len(self._clienti)):
            if self._clienti[idx] == client_nou:
                '''
                self._clienti[idx] = client_nou
                '''

                self._clienti[idx].set_nume(client_nou.get_nume())
                self._clienti[idx].set_cnp(client_nou.get_cnp())
                return

        raise RepoError('client inexistent!\n')

    #operatie de tipul D (Delete), care modifica lista de clienti prin eliminarea (stergerea) unui element din lista de clienti din repository (asta daca clientul respectiv se afla/gaseste in repo)
    #aceasta operatie poate modifica marimea repository-ului spre deosebire de operatia de modificare (adica se poate face decrementul cu 1 a numarului de clienti din repository spre deosebire de operatia adauga din R unde se putea ca acest numar sa se incrementeze cu 1)
    def sterge_dupa_id(self, id_client):
        #metoda/functie care cauta un client in repositoy care sa aiba id-ul id_client si daca il gaseste, atunci il elimina (sterge) din lista de clienti din repository
        #date de intrare: id_client - intreg care reprezinta id-ul clientului pe care dorim sa il inlaturam din lista de clienti din repository
        #date de iesire: -, daca clientul cu id-ul id_client a fost gasit si implicit sters din repository cu ajutorul functiei predefinite del
        #               exceptie de tipul RepoError cu mesajul de eroare 'client inexistent!\n' in caz contrar

        for idx in range(len(self._clienti)):
            if self._clienti[idx].get_id_client() == id_client:
                del self._clienti[idx]
                return

        raise RepoError('client inexistent!\n')