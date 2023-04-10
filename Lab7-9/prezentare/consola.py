#din pachetul erori, modulul exceptii, importam clasele de obiecte ValidError si RepoError (ambele au un comportanent similar cu exceptia Exception)
from erori.exceptii import ValidError, RepoError

class LucruMemorieFisiere:
    def __init__(self):
        self.__memorie = True

    def __citire_optiune_stocare_date(self):
        print('Alegeti modul in care sa functioneze aplicatia:')
        print('*memorie - cu date salvate in memorie')
        print('*fisiere - cu date salvate in fisier\n')
        while True:
            cmd = input('>>>')
            if cmd.lower() == 'fisiere':
                self.__memorie = False
            elif cmd.lower() != 'memorie':
                print('Comanda invalida!\n')
                print('Reintroduceti modul in care sa functioneze aplicatia:')
                print('*memorie - cu date salvate in memorie')
                print('*fisiere - cu date salvate in fisier\n')
                continue
            break

    def verifica_lucru_memorie(self):
        self.__citire_optiune_stocare_date()
        return self.__memorie

class UI:
    #clasa in care definim toate functiile de interfata cu utilizatorul din cadrul aplicatiei
    #aceste functii nu au nici date de intrare si nici date de iesire (rezultate), ci ele doar citesc sau afiseaza tiparesc date
    #de asemenea ele pot sa apeleze alte functii/metode din modulul servicii (pachetul business)

    #metode pentru manipularea listei de filme
    def __ui_generare_filme(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        self.__srv_filme.generare_filme()
        print()

    def __ui_adauga_film(self, argumente_comanda):
        if len(argumente_comanda) != 6:
            raise Exception('numar invalid de argumente comanda!\n')

        id_film = int(argumente_comanda[0])
        titlu = argumente_comanda[1]
        descriere = argumente_comanda[2]
        gen = argumente_comanda[3]
        an_lansare = int(argumente_comanda[4])
        durata = int(argumente_comanda[5])

        self.__srv_filme.adauga_film(id_film, titlu, descriere, gen, an_lansare, durata)
        print()

    def __ui_afisare_lista_filme(self, lista_filme):
        idx_film = 1
        for film in lista_filme:
            print('#', end='')
            print(idx_film)
            print(film)
            idx_film += 1

    def __ui_afisare_filme(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_filme.nr_filme():
            print('Nu exista filme in repository!\n')
            return

        print('Filmele din repository sunt:')
        lista_filme = self.__srv_filme.get_filme()
        self.__ui_afisare_lista_filme(lista_filme)

    def __ui_sterge_film(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] == ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_filme.nr_filme():
            print('Nu exista filme in repository!\n')
            return

        id_film = int(argumente_comanda[0])

        self.__srv_filme.sterge_film(id_film)
        print()

    def __ui_modifica_film(self, argumente_comanda):
        if len(argumente_comanda) != 6:
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_filme.nr_filme():
            print('Nu exista filme in repository!\n')
            return

        id_film = int(argumente_comanda[0])
        titlu = argumente_comanda[1]
        descriere = argumente_comanda[2]
        gen = argumente_comanda[3]
        an_lansare = int(argumente_comanda[4])
        durata = int(argumente_comanda[5])

        self.__srv_filme.modifica_flim(id_film, titlu, descriere, gen, an_lansare, durata)
        print()

    def __ui_cauta_film(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda == ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_filme.nr_filme():
            print('Nu exista filme in repository!\n')
            return

        id_film = int(argumente_comanda[0])

        film = self.__srv_filme.cauta_film(id_film)
        print('Filmul cu id-ul', id_film, 'este:')
        print(film)

    #metode pentru manipularea listei de clienti
    def __ui_generare_clienti(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        self.__srv_clienti.generare_clienti()
        print()

    def __ui_adauga_client(self, argumente_comanda):
        if len(argumente_comanda) != 3:
            raise Exception('numar invalid de argumente comanda!\n')

        id_client = int(argumente_comanda[0])
        nume = argumente_comanda[1]
        cnp = int(argumente_comanda[2])

        self.__srv_clienti.adauga_client(id_client, nume, cnp)
        print()

    def __ui_afisare_lista_clienti(self, lista_clienti):
        idx_client = 1
        for client in lista_clienti:
            print('#', end='')
            print(idx_client)
            print(client)
            idx_client += 1

    def __ui_afisare_clienti(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_clienti.nr_clienti():
            print('Nu exista clienti in repository!\n')
            return

        print('Clientii din repository sunt:')
        lista_clienti = self.__srv_clienti.get_clienti()
        self.__ui_afisare_lista_clienti(lista_clienti)

    def __ui_sterge_client(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] == ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_clienti.nr_clienti():
            print('Nu exista clienti in repository!\n')
            return

        id_client = int(argumente_comanda[0])

        self.__srv_clienti.sterge_client(id_client)
        print()

    def __ui_modifica_client(self, argumente_comanda):
        if len(argumente_comanda) != 3:
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_clienti.nr_clienti():
            print('Nu exista clienti in repository!\n')
            return

        id_client = int(argumente_comanda[0])
        nume = argumente_comanda[1]
        cnp = int(argumente_comanda[2])

        self.__srv_clienti.modifica_client(id_client, nume, cnp)
        print()

    def __ui_cauta_client(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] == ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_clienti.nr_clienti():
            print('Nu exista clienti in repository!\n')
            return

        id_client = int(argumente_comanda[0])

        client = self.__srv_clienti.cauta_client(id_client)
        print('Clientul cu id-ul', id_client, 'este:')
        print(client)

    #metode pentru inchirieri/returnari filme
    def __ui_inchiriere_film(self, argumente_comanda):
        if len(argumente_comanda) != 4:
            raise Exception('numar invalid de argumente comanda!\n')

        str = ''
        if not self.__srv_filme.nr_filme():
            str += 'Nu exista filme in repository!\n'
        if not self.__srv_clienti.nr_clienti():
            str += 'Nu exista clienti in repository!\n'
        if len(str):
            print(str)
            return

        id_inchiriere = int(argumente_comanda[0])
        id_film = int(argumente_comanda[1])
        id_client = int(argumente_comanda[2])

        self.__srv_inchirieri.inchiriere_film(id_inchiriere, id_film, id_client, argumente_comanda[3].split('.'))
        print()

    def __ui_returnare_film(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] == ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_inchirieri.nr_inchirieri():
            print('Nu exista inchirieri de filme in repository!\n')
            return

        id_inchiriere = int(argumente_comanda[0])

        self.__srv_inchirieri.returnare_film(id_inchiriere)
        print()

    def __ui_modifica_inchiriere(self, argumente_comanda):
        if len(argumente_comanda) != 4:
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_inchirieri.nr_inchirieri():
            print('Nu exista inchirieri de filme in repository!\n')
            return

        id_inchiriere = int(argumente_comanda[0])
        id_film = int(argumente_comanda[1])
        id_client = int(argumente_comanda[2])

        self.__srv_inchirieri.modifica_inchiriere(id_inchiriere, id_film, id_client, argumente_comanda[3].split('.'))
        print()

    def __ui_cauta_inchiriere(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] == ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_inchirieri.nr_inchirieri():
            print('Nu exista inchirieri de filme in repository!\n')
            return

        id_inchiriere = int(argumente_comanda[0])

        inchiriere = self.__srv_inchirieri.cauta_inchiriere(id_inchiriere)
        print('Inchirierea cu id-ul', id_inchiriere, 'este:')
        print(inchiriere)

    def __ui_afisare_lista_inchirieri(self, lista_inchirieri):
        idx_inchiriere = 1
        for inchiriere in lista_inchirieri:
            print('#', end='')
            print(idx_inchiriere)
            print(inchiriere)
            idx_inchiriere += 1

    def __ui_afisare_inchirieri(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        if not self.__srv_inchirieri.nr_inchirieri():
            print('Nu exista inchirieri de filme in repository!\n')
            return

        print('Inchirierile din repository sunt:')
        lista_inchirieri = self.__srv_inchirieri.get_inchirieri()
        self.__ui_afisare_lista_inchirieri(lista_inchirieri)

    #metoda pentru gestiunea rapoartelor filme/clienti
    def __afisare_lista_clienti_dupa_nume(self, lista_clienti):
        for idx in range(len(lista_clienti)):
            print('Clientul #', end = '')
            print(idx + 1)
            print(lista_clienti[idx], end = '\n\n')

    def __afisare_lista_clienti_nrFilme(self, lista_clienti_nrFilme):
        for idx in range(len(lista_clienti_nrFilme)):
            print('Clientul #', end = '')
            print(idx + 1)
            print(lista_clienti_nrFilme[idx][0])
            nr_filme = lista_clienti_nrFilme[idx][1]
            if nr_filme == 1:
                print('cu un singur film inchiriat')
            else:
                print('cu', nr_filme, 'filme inchiriate')
            print()

    def __ui_raport_clienti_1(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        err = ''

        if not self.__srv_filme.nr_filme():
            err += 'Nu exista filme in repository!\n'

        if not self.__srv_clienti.nr_clienti():
            err += 'Nu exista clienti in repository!\n'

        if not self.__srv_inchirieri.nr_inchirieri():
            err += 'Nu exista inchirieri de filme in repository!\n'

        if len(err):
            print(err)
            return

        lista_clienti = self.__srv_rapoarte.raport_clienti_1_ordonat_nume()
        print('Clientii cu filme inchiriate ordonati lexicografic (alfabetic) dupa nume sunt:')
        self.__afisare_lista_clienti_dupa_nume(lista_clienti)

        lista_clienti_nrFilme = self.__srv_rapoarte.raport_clienti_1_ordonat_nr_filme()
        print('Clientii cu filme inchiriate ordonati crescator dupa numarul de filme inchiriate sunt:')
        self.__afisare_lista_clienti_nrFilme(lista_clienti_nrFilme)

    def __afisare_cele_mai_inchiriate_filme(self, lista_filme_nrInchirieri):
        max_inchirieri = lista_filme_nrInchirieri[0][1]
        for idx in range(len(lista_filme_nrInchirieri)):
            nr_inchirieri = lista_filme_nrInchirieri[idx][1]
            if nr_inchirieri != max_inchirieri:
                break
            print('#', end = '')
            print(idx + 1)
            print(lista_filme_nrInchirieri[idx][0])
            if nr_inchirieri == 1:
                print('cu o singura inchiriere')
            else:
                print('cu', nr_inchirieri, 'inchirieri')
            print()

    def __ui_raport_filme(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        err = ''

        if not self.__srv_filme.nr_filme():
            err += 'Nu exista filme in repository!\n'

        if not self.__srv_clienti.nr_clienti():
            err += 'Nu exista clienti in repository!\n'

        if not self.__srv_inchirieri.nr_inchirieri():
            err += 'Nu exista inchirieri de filme in repository!\n'

        if len(err):
            print(err)
            return

        lista_filme_nrInchirieri = self.__srv_rapoarte.raport_filme()
        print('Cele mai inchiriate filme sunt:')
        self.__afisare_cele_mai_inchiriate_filme(lista_filme_nrInchirieri)

    def __afisare_lista_clienti(self, lista_clienti_nrInchirieri):
        nr = int((30 * len(lista_clienti_nrInchirieri)) / 100)
        for idx in range(nr):
            print('Clientul #', end = '')
            print(idx + 1)
            client = lista_clienti_nrInchirieri[idx][0]
            print(client.get_nume())
            nr_filme = lista_clienti_nrInchirieri[idx][1]
            if nr_filme == 1:
                print('cu un singur film inchiriat')
            else:
                print('cu', nr_filme, 'filme inchiriate')
            print()

    def __ui_raport_clienti_2(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        err = ''

        if not self.__srv_filme.nr_filme():
            err += 'Nu exista filme in repository!\n'

        if not self.__srv_clienti.nr_clienti():
            err += 'Nu exista clienti in repository!\n'

        if not self.__srv_inchirieri.nr_inchirieri():
            err += 'Nu exista inchirieri de filme in repository!\n'

        if len(err):
            print(err)
            return

        lista_clienti_nrInchirieri = self.__srv_rapoarte.raport_clienti_2()

        nr = int((30 * len(lista_clienti_nrInchirieri)) / 100)

        print('Primi', end = ' ')
        print(nr, end = ' ')
        print('clienti (30% din', end = ' ')
        print(len(lista_clienti_nrInchirieri), end = ') ')
        print('cu cele mai multe filme inchiriate sunt:')
        self.__afisare_lista_clienti(lista_clienti_nrInchirieri)

        if not nr:
            print('-')
            print()

    #metoda pentru terminarea executiei aplicatiei
    def __ui_iesire_app(self, argumente_comanda):
        #functie care opreste aplicatia de tip interfata cu utilizatorul
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argumente comanda!\n')

        print('Iesire din aplicatie...') #mesaj catre utilizator care sa semnaleze ichiderea aplicatiei
        exit() #terminarea normala a programului (fara a furniza vreun cod de retur)

    #metoda pentru afisarea in consola a meniului de comenzi disponibile utilizatorului
    def __ui_afisare_meniu_aplicatie(self, argumente_comanda):
        #functie care afiseaza meniul de comenzi al aplicatiei
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        print()
        self.__afisare_meniu_aplicatie()
        print()

    def __ui_afisare_meniu_clienti(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        print()
        self.__afisare_meniu_comenzi_clienti()
        print()

    def __ui_afisare_meniu_filme(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        print()
        self.__afisare_meniu_comenzi_filme()
        print()

    def __ui_afisare_meniu_inchirieri(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        print()
        self.__afisare_meniu_comenzi_inchirieri()
        print()

    def __ui_afisare_meniu_rapoarte(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        print()
        self.__afisare_meniu_comenzi_rapoarte()
        print()

    def __ui_afisare_meniu_aditional(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] != ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        print()
        self.__afisare_meniu_comenzi_aditionale()

    def __ui_afisare_lista_filme_inchiriate(self, lista_filme_inchiriate, durata):
        print('Filmele inchiriate cu durata totala de rulare mai mare de', durata, 'minute sunt:')
        idx = 0
        for film in lista_filme_inchiriate:
            if film.get_durata() > durata:
                idx += 1
                print('#', end = '')
                print(idx)
                print(film)

    def __ui_raport_filme_2(self, argumente_comanda):
        if len(argumente_comanda) != 1 or (len(argumente_comanda) == 1 and argumente_comanda[0] == ''):
            raise Exception('numar invalid de argusmente comanda!\n')

        err = ''

        if not self.__srv_filme.nr_filme():
            err += 'Nu exista filme in repository!\n'

        if not self.__srv_clienti.nr_clienti():
            err += 'Nu exista clienti in repository!\n'

        if not self.__srv_inchirieri.nr_inchirieri():
            err += 'Nu exista inchirieri de filme in repository!\n'

        if len(err):
            print(err)
            return

        try:
            durata = int(argumente_comanda[0])
        except ValueError as ve:
            print(str(ve))
            return
        except TypeError as te:
            print(str(te))
            return
        except Exception as ex:
            print(str(ex))
            return

        lista_filme_inchiriate = self.__srv_rapoarte.raport_filme_2()
        self.__ui_afisare_lista_filme_inchiriate(lista_filme_inchiriate, durata)

    def __init__(self, srv_filme, srv_clienti, srv_inchirieri, srv_rapoarte):
        #constructor care initializeaza la creare cele 3 campuri/componente ale unui obiect de clasa UI (nou creat)
        #campurile unui obiect de clasa UI sunt private (ele nu pot fi accesate din exteriorul clasei, ci doar din interiorul acesteia)

        self.__srv_filme = srv_filme
        self.__srv_clienti = srv_clienti
        self.__srv_inchirieri = srv_inchirieri
        self.__srv_rapoarte = srv_rapoarte
        self.__comenzi = {'generate_filme'    : self.__ui_generare_filme,
                          'add_film'          : self.__ui_adauga_film,
                          'del_film'          : self.__ui_sterge_film,
                          'modify_film'       : self.__ui_modifica_film,
                          'search_film'       : self.__ui_cauta_film,
                          'print_filme'       : self.__ui_afisare_filme,
                          'generate_clienti'  : self.__ui_generare_clienti,
                          'add_client'        : self.__ui_adauga_client,
                          'del_client'        : self.__ui_sterge_client,
                          'modify_client'     : self.__ui_modifica_client,
                          'search_client'     : self.__ui_cauta_client,
                          'print_clienti'     : self.__ui_afisare_clienti,
                          'inchiriere'        : self.__ui_inchiriere_film,
                          'returnare'         : self.__ui_returnare_film,
                          'modify_inchiriere' : self.__ui_modifica_inchiriere,
                          'search_inchiriere' : self.__ui_cauta_inchiriere,
                          'print_inchirieri'  : self.__ui_afisare_inchirieri,
                          'raport_clienti_1'  : self.__ui_raport_clienti_1,
                          'raport_filme'      : self.__ui_raport_filme,
                          'raport_clienti_2'  : self.__ui_raport_clienti_2,
                          'raport_filme_2'    : self.__ui_raport_filme_2,
                          'meniu_principal'   : self.__ui_afisare_meniu_aplicatie,
                          'meniu_filme'       : self.__ui_afisare_meniu_clienti,
                          'meniu_clienti'     : self.__ui_afisare_meniu_filme,
                          'meniu_inchirieri'  : self.__ui_afisare_meniu_inchirieri,
                          'meniu_rapoarte'    : self.__ui_afisare_meniu_rapoarte,
                          'meniu_aditional'   : self.__ui_afisare_meniu_aditional,
                          'exit'              : self.__ui_iesire_app}

    def __afisare_meniu_comenzi_filme(self):
        print('\nMeniu comenzi filme:')
        print('*generate_filme    - genereaza filme in mod aleator')
        print('*add_film          - adauga un film nou la lista de filme din repository')
        print('*del_film          - sterge un film cu un id dat din lista de filme')
        print('*modify_film       - modifica informatiile unui film deja existent')
        print('*search_film       - cauta film dupa un id dat')
        print('*print_filme       - afiseaza lista de filme din repository')

    def __afisare_meniu_comenzi_clienti(self):
        print('\nMeniu comenzi clienti:')
        print('*generate_clienti  - genereaza clienti in mod aleator')
        print('*add_client        - adauga un client nou la lista de clienti din repository')
        print('*del_client        - sterge un client cu un id dat din lista de clienti')
        print('*modify_client     - modifica informatiile unui client deja existent')
        print('*search_client     - cauta un client dupa un id dat')
        print('*print_clienti     - afiseaza lista de clienti din repository')

    def __afisare_meniu_comenzi_inchirieri(self):
        print('\nMeniu inchirieri/returnari filme: ')
        print('*inchiriere        - inchiriere film cu id dat de catre un client pentru care se citeste id-ul')
        print('*returnare         - returnare film cu id dat de catre un client pentru care se citeste id-ul')
        print('*modify_inchiriere - modifica informatiile unei inchirieri deja exsitente')
        print('*search_inchiriere - cauta o inchiriere dupa un id dat')
        print('*print_inchirieri  - afiseaza toate inchirierile inregistrate in repository')

    def __afisare_meniu_comenzi_rapoarte(self):
        print('\nMeniu rapoarte:')
        print('*raport_clienti_1  - clienti cu filme inchiriate ordonat dupa: nume, dupa numarul de filme inchiriate')
        print('*raport_filme      - cele mai inchiriate filme')
        print('*raport_clienti_2  - primi 30% clienti cu cele mai multe filme (nume client si numarul de filme inchiriate)')
        print('*raport_filme_2    - afiseaza toate filmele inchiriate care au durata mai mare decat un numar citit')

    def __afisare_meniu_comenzi_aditionale(self):
        print('\nMeniu comenzi aditionale:')
        print('*meniu_principal   - afisare meniu comenzi')
        print('*meniu_filme       - afiseaza comenzile din meniul filme')
        print('*meniu_clienti     - afiseaza comenzile din meniul clienti')
        print('*meniu_inchirieri  - afiseaza comenzile din meniul inchirieri')
        print('*meniu rapoarte    - afiseaza comenzile din meniul rapoarte')
        print('*meniu_aditional   - afiseaza comenzile din meniul de comenzi aditionale')
        print('*exit              - iesirea din aplicatie', end='\n\n')

    def __afisare_meniu_aplicatie(self):
        #procedura ce afiseaza meniul de optiuni destinat utilizatorului
        #fiecarei comenzi ii corespunde o functionalitate din lista de functionalitati a programului

        print('Meniu aplicatie')
        self.__afisare_meniu_comenzi_filme()
        self.__afisare_meniu_comenzi_clienti()
        self.__afisare_meniu_comenzi_inchirieri()
        self.__afisare_meniu_comenzi_rapoarte()
        self.__afisare_meniu_comenzi_aditionale()

    def __comanda_split(self, comanda):
        nume_comanda = comanda.split()[0].lower()
        argumente_comanda = comanda.split()[1:]
        str_argumente_comanda = ''
        idx = 0
        for argument in argumente_comanda:
            str_argumente_comanda += argument
            if argument[len(argument) - 1] != ',' and idx != len(argumente_comanda) - 1:
                str_argumente_comanda += ' '
            idx += 1
        argumente_comanda = str_argumente_comanda.split(',')
        return [nume_comanda, argumente_comanda]

    ##################################################
    def __ui_adauga_inchirieri_repo(self):
        self.__srv_inchirieri.adauga_inchirieri_repo()
    ##################################################

    def run_app(self):
        #functie de interfata cu utilizatorul care simuleaza aplicatia de tip consola
        #exemplu cititre cu batch: print_filme; add_film 6, IT, Penniwise the killer clown, horror, 2017, 135; print_filme; add_film 3, The Gift, bla bla bla bla, thriller psihologic, 1996, 86; print_filme; del_film 6; print_filme; modify_film 3, The Hobbit, Bilbo Baggins is going on an aventure, aventura, 2006, 205; print_filme
        #                          print_clienti; add_client 4, Spiridon Dragos Stefan, 5382753268314;  add_client 0, Morish Robert, 8673074278323; print_clienti; search_client -4; search_client 7; search_client 0; search_client 4; del_client 3; del_client 4; print_clienti; del_client 0; print_clienti

        ###################################
        self.__ui_adauga_inchirieri_repo()
        ###################################

        self.__afisare_meniu_aplicatie()
        while True: #bucla infinita (ciclu infinit)
            cmd = input('>>>')
            if cmd == ' ' * len(cmd):
                print()
                continue
            cmd = cmd.strip()
            lista_comenzi = cmd.split(';')
            for comanda in lista_comenzi:
                nume_comanda, argumente_comanda = self.__comanda_split(comanda)
                if nume_comanda in self.__comenzi:
                    try:
                        self.__comenzi[nume_comanda](argumente_comanda)
                    except ValueError as ve:
                        print(str(ve))
                        print()
                    except RepoError as re:
                        print(str(re))
                        print()
                    except ValidError as ve:
                        print(str(ve))
                        print()
                    except Exception as ex:
                        print(str(ex))
                        print()
                else:
                    print('Comanda invalida!\n')
