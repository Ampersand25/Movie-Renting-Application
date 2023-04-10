#din pachetul domeniu, modulul de entitati (film_entitate si client_entitate), importam clasele de obiecte Film si Client
from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
from domeniu.inchiriere_entitate import Inchiriere

#din pachetul validare, modulul validatori, importam clasele de obiecte ValidatorFilm si ValidatorClient
from validare.validator_film import ValidatorFilm
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere

#din pachetul erori, modulul exceptii, importam obiectele de clasa ValidError si RepoError
from erori.exceptii import ValidError
from erori.exceptii import RepoError

#din pachetul infrastructura, modulul repos, importam obiectele de clasa RepositoryFilme si respectiv RepositoryClienti
from infrastructura.repo_filme import RepositoryFilme
from infrastructura.repo_clienti import RepositoryClienti
from infrastructura.repo_inchirieri import RepositoryInchirieri

#din pachetul business, modulul servicii, importam obiectele de clasa ServiceFilme si respectiv ServiceClienti
from business.servicii_filme import ServiceFilme
from business.servicii_clienti import ServiceClienti
from business.servicii_inchirieri import ServiceInchirieri

class Teste:
    #metodele din clasa Teste nu au nici date de intrare, nici date de iesire
    #ele verifica doar corectitudinea functiilor/metodelor implementate la nivel de clase si a unor posibile date introduse de catre utilizator pentru campurile unor obiecte de clasa definita la nivelul modulului entitati

    def __ruleaza_teste_film(self):
        #metoda care verifica corectitudinea metodelor din clasa Film

        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        assert film.get_id_film() == id_film
        assert film.get_titlu() == titlu
        assert film.get_descriere() == descriere
        assert film.get_gen() == gen
        assert film.get_an_lansare() == an_lansare
        assert film.get_durata() == durata
        assert str(film) == 'id: 21\ntitlu: I Am Mother\ndescriere: We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.\ngen: sci-fi\nan lansare: 2019\ndurata totala (minute): 113\n'

        titlu_nou = 'IT'
        film.set_titlu(titlu_nou)
        assert film.get_titlu() == titlu_nou
        assert str(film) == 'id: 21\ntitlu: IT\ndescriere: We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.\ngen: sci-fi\nan lansare: 2019\ndurata totala (minute): 113\n'

        descriere_noua = 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        film.set_descriere(descriere_noua)
        assert film.get_descriere() == descriere_noua
        assert str(film) == 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: sci-fi\nan lansare: 2019\ndurata totala (minute): 113\n'

        gen_nou = 'horror'
        film.set_gen(gen_nou)
        assert film.get_gen() == gen_nou
        assert str(film) == 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: horror\nan lansare: 2019\ndurata totala (minute): 113\n'

        an_lansare_nou = 2017
        film.set_an_lansare(an_lansare_nou)
        assert film.get_an_lansare() == an_lansare_nou
        assert str(film) == 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: horror\nan lansare: 2017\ndurata totala (minute): 113\n'

        durata_noua = 135
        film.set_durata(durata_noua)
        assert film.get_durata() == durata_noua
        assert str(film) == 'id: 21\ntitlu: IT\ndescriere: In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.\ngen: horror\nan lansare: 2017\ndurata totala (minute): 135\n'

        alt_film = Film(id_film, '', '', '', 0, 0)

        assert film == alt_film
        assert film.__eq__(alt_film)
        assert id(film) != id(alt_film)

        alt_film = Film(id_film + 1, '', '', '', 0, 0)

        assert film != alt_film
        assert not film.__eq__(alt_film)
        assert id(film) != id(alt_film)

    def __ruleaza_teste_client(self):
        #metoda care verifica corectitudinea metodelor din clasa Client

        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        assert client.get_id_client() == id_client
        assert client.get_nume() == nume
        assert client.get_cnp() == cnp
        assert str(client) == 'id: 35\nnume: Popescu Mihai\ncnp: 1951124682471\n'

        nume_nou = 'Ionescu Alexandru'
        client.set_nume(nume_nou)

        assert client.get_id_client() == id_client
        assert client.get_nume() == nume_nou
        assert client.get_cnp() == cnp
        assert str(client) == 'id: 35\nnume: Ionescu Alexandru\ncnp: 1951124682471\n'

        alt_client = Client(id_client, '', cnp - 1)

        assert client == alt_client
        assert client.__eq__(alt_client)
        assert id(client) != id(alt_client)

        alt_client = Client(id_client + 1, '', cnp)

        assert client == alt_client
        assert client.__eq__(alt_client)
        assert id(client) != id(alt_client)

        alt_client = Client(id_client, '', cnp)

        assert client == alt_client
        assert client.__eq__(alt_client)
        assert id(client) != id(alt_client)

        alt_client = Client(id_client - 1, '', cnp + 1)

        assert client != alt_client
        assert not client.__eq__(alt_client)
        assert id(client) != id(alt_client)

    def __ruleaza_teste_domeniu(self):
        #metoda care apeleaza alte doua metode care ruleaza teste pentru cele doua clase de entitati: Film si Client

        self.__ruleaza_teste_film()   #metoda care testeaza obiectele (filmele) din clasa Film
        self.__ruleaza_teste_client() #metoda care testeaza obiectele (clientii) din clasa Client
        #aceste doua metode nu arunca exceptii (nu se trateaza cazurile de eroare cu try except deoarece nu se testeaza functii/metode ci doar campuri/componente din cadrrul unei clase de obiecte)

    def __ruleaza_teste_validare_film(self):
        #metoda care valideaza campurile dintr-ul obiect de clasa Film

        valid = ValidatorFilm()

        film_rau = Film(-5, '', '', '', 1264, 1e+3)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\ndurata totala de rulare invalida!\n'

        film_rau = Film(55, '', '', '', 1264, 59)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'titlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\ndurata totala de rulare invalida!\n'

        film_rau = Film(-31, '', '', '', 2020, 211)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\ndurata totala de rulare invalida!\n'

        film_rau = Film(-1, '', '', '', 2021, 83)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\n'

        film_rau = Film(3, '', '', '', 2016, -64)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'titlu invalid!\ndescriere invalida!\ngen invalid!\ndurata totala de rulare invalida!\n'

        film_rau = Film(3, '', '', '', -7, 210)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'titlu invalid!\ndescriere invalida!\ngen invalid!\nan de lansare invalid!\n'

        film_rau = Film(-67377, '', '', '', 1901, 158)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\n'

        film_rau = Film(0, '', '', '', 1987, 60)
        try:
            valid.valideaza(film_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'titlu invalid!\ndescriere invalida!\ngen invalid!\n'

    def __ruleaza_teste_validare_client(self):
        # metoda care valideaza campurile dintr-ul obiect de clasa Client

        valid = ValidatorClient()

        client_rau = Client(-852, '', 741786776282)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id client invalid!\nnume invalid!\ncnp invalid!\n'

        client_rau = Client(-46, 'Pruteanu Robert', 5011014681833)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id client invalid!\n'

        client_rau = Client(61, '', 4031201300164)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'nume invalid!\n'

        client_rau = Client(27, 'Anton Felicia', 1e+13)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'cnp invalid!\n'

        client_rau = Client(-1, '', 1971030867010)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id client invalid!\nnume invalid!\n'

        client_rau = Client(-96, 'Vancea Alexandru', 999999999999)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id client invalid!\ncnp invalid!\n'

        client_rau = Client(0, '', -7317428638319)
        try:
            valid.valideaza(client_rau)
            assert False
        except ValidError as ve:
            assert str(ve) == 'nume invalid!\ncnp invalid!\n'

        client_bun = Client(17, 'Oniga Maria', 6010623947184)
        try:
            valid.valideaza(client_bun)
            assert True
        except ValidError:
            assert False

    def __ruleaza_teste_validare(self):
        #metoda care valideaza corectitudinea campurilor din clasele aferente celor doua entitati: Film si Client

        self.__ruleaza_teste_validare_film()   #validam campurile unui obiect (film) din clasa Film
        self.__ruleaza_teste_validare_client() #validam campurile unui obiect (client) din clasa Client
        #toate exceptiile aruncate (returnate/furnizate) de aceste doua metode/functii vor fi de tipul ValidError (adica de tipul Exception, deoarece clasa ValidError are acelasi efect ca si exceptia Exception)

    def __ruleaza_teste_repo_filme(self):
        #validam toate cele 7 operatii permise pe un repository de filme

        repo = RepositoryFilme()
        assert not len(repo)

        id_film = 21
        titlu = 'I Am Mother'
        descriere = 'We follow a young girl named Daughter, who lives in a post-apocalyptic bunker with her robot, named Mother, whose purpose is to aid the repopulation of Earth.'
        gen = 'sci-fi'
        an_lansare = 2019
        durata = 113
        film = Film(id_film, titlu, descriere, gen, an_lansare, durata)

        repo.adauga(film)
        assert len(repo) == 1

        gasit = repo.cauta_dupa_id(film.get_id_film())
        assert gasit.get_titlu() == titlu
        assert gasit.get_descriere() == descriere
        assert gasit.get_gen() == gen
        assert gasit.get_an_lansare() == an_lansare
        assert gasit.get_durata() == durata

        try:
            repo.adauga(film)
            assert False
        except RepoError as re:
            assert str(re) == 'film deja existent!\n'

        try:
            repo.cauta_dupa_id(film.get_id_film() + 1)
            assert False
        except RepoError as re:
            assert str(re) == 'film inexistent!\n'

        film_nou = Film(film.get_id_film(), 'IT', 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.', 'horror', 2017, 135)
        repo.modifica(film_nou)
        gasit = repo.cauta_dupa_id(film_nou.get_id_film())

        assert gasit.get_titlu() == 'IT'
        assert gasit.get_descriere() == 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        assert gasit.get_gen() == 'horror'
        assert gasit.get_an_lansare() == 2017
        assert gasit.get_durata() == 135

        film_nou_rau = Film(film.get_id_film() - 1, 'IT', 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.', 'horror', 2017, 135)
        try:
            repo.modifica(film_nou_rau)
            assert False
        except RepoError as re:
            assert str(re) == 'film inexistent!\n'

        lista_filme = repo.get_all()
        assert len(lista_filme) == 1
        assert lista_filme[0].get_titlu() == 'IT'
        assert lista_filme[0].get_descriere() == 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.'
        assert lista_filme[0].get_gen() == 'horror'
        assert lista_filme[0].get_an_lansare() == 2017
        assert lista_filme[0].get_durata() == 135

        repo.sterge_dupa_id(film.get_id_film())
        assert not len(repo)

        try:
            repo.sterge_dupa_id(film.get_id_film())
            assert False
        except RepoError as re:
            assert str(re) == 'film inexistent!\n'

    def __ruleaza_teste_repo_clienti(self):
        #validam toate cele 7 operatii permise pe un repository de clienti

        repo = RepositoryClienti()
        assert not len(repo)

        id_client = 35
        nume = 'Popescu Mihai'
        cnp = 1951124682471
        client = Client(id_client, nume, cnp)

        repo.adauga(client)
        assert len(repo) == 1

        gasit = repo.cauta_dupa_id(client.get_id_client())
        assert gasit.get_nume() == nume
        assert gasit.get_cnp() == cnp

        try:
            repo.adauga(client)
            assert False
        except RepoError as re:
            assert str(re) == 'client deja existent!\n'

        try:
            repo.cauta_dupa_id(client.get_id_client() - 1)
            assert False
        except RepoError as re:
            assert str(re) == 'client inexistent!\n'

        client_nou = Client(client.get_id_client(), 'Ionescu Alexandru', 1951124682471)
        repo.modifica(client_nou)
        gasit = repo.cauta_dupa_id(client_nou.get_id_client())

        assert gasit.get_nume() == 'Ionescu Alexandru'
        assert gasit.get_cnp() == 1951124682471

        client_nou_rau = Client(client.get_id_client() + 1, 'Ionescu Alexandru', 1970519831755)
        try:
            repo.modifica(client_nou_rau)
            assert False
        except RepoError as re:
            assert str(re) == 'client inexistent!\n'

        lista_clienti = repo.get_all()
        assert len(lista_clienti) == 1
        assert lista_clienti[0].get_nume() == 'Ionescu Alexandru'
        assert lista_clienti[0].get_cnp() == 1951124682471

        repo.sterge_dupa_id(client.get_id_client())
        assert not len(repo)

        try:
            repo.sterge_dupa_id(client.get_id_client())
            assert False
        except RepoError as re:
            assert str(re) == 'client inexistent!\n'

    def __ruleaza_teste_repo(self):
        #metoda/functie privata care testeaza cele doua repository-uri create de catre programator

        self.__ruleaza_teste_repo_filme()   #se face testarea repository-ului de filme prin rulare de teste cu assert si prindere de exceptii cu instructiunea try except
        self.__ruleaza_teste_repo_clienti() #se face testarea repository-ului de clienti prin rularea de teste cu assert si prinderea de exceptii cu instrictiunea try except
        #toate exceptiile ridicate folosind instructiunea raise urmata de tipul exceptiei, vor fi de tipul RepoError (clasa definita de catre programator echivalenta cu exceptia predefinita Exception)

    def __ruleaza_teste_service_filme(self):
        valid = ValidatorFilm()
        repo_filme = RepositoryFilme()
        repo_inchirieri = RepositoryInchirieri()
        srv = ServiceFilme(valid, repo_filme, repo_inchirieri)

        id_film = 13
        titlu = 'Se7en'
        descriere = 'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.'
        gen = 'crime'
        an_lansare = 1995
        durata = 127
        srv.adauga_film(id_film, titlu, descriere, gen, an_lansare, durata)

        filme = srv.get_filme()
        assert len(filme) == 1

        try:
            srv.adauga_film(id_film, titlu, descriere, gen, an_lansare, durata)
            assert False
        except RepoError as re:
            assert str(re) == 'film deja existent!\n'

        try:
            srv.adauga_film(-id_film, titlu, descriere, gen, -an_lansare, -durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\nan de lansare invalid!\ndurata totala de rulare invalida!\n'

        try:
            srv.adauga_film(-id_film, titlu, descriere, gen, -an_lansare, durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\nan de lansare invalid!\n'

        try:
            srv.adauga_film(-id_film, titlu, descriere, gen, an_lansare, -durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\ndurata totala de rulare invalida!\n'

        try:
            srv.adauga_film(id_film, titlu, descriere, gen, -an_lansare, -durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'an de lansare invalid!\ndurata totala de rulare invalida!\n'

        try:
            srv.adauga_film(id_film, titlu, descriere, gen, an_lansare, -durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'durata totala de rulare invalida!\n'

        try:
            srv.adauga_film(id_film, titlu, descriere, gen, -an_lansare, durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'an de lansare invalid!\n'

        try:
            srv.adauga_film(-id_film, titlu, descriere, gen, an_lansare, durata)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id film invalid!\n'

    def __ruleaza_teste_service_clienti(self):
        valid = ValidatorClient()
        repo_clienti = RepositoryClienti()
        repo_inchirieri = RepositoryInchirieri()
        srv = ServiceClienti(valid, repo_clienti, repo_inchirieri)

        id_client = 7
        nume = 'Pop Alexandra'
        cnp = 6070526963784
        srv.adauga_client(id_client, nume, cnp)

        clienti = srv.get_clienti()
        assert len(clienti) == 1

        try:
            srv.adauga_client(id_client, nume, cnp)
            assert False
        except RepoError as re:
            assert str(re) == 'client deja existent!\n'

        try:
            srv.adauga_client(-id_client, nume, -cnp)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id client invalid!\ncnp invalid!\n'

        try:
            srv.adauga_client(-id_client, nume, cnp)
            assert False
        except ValidError as ve:
            assert str(ve) == 'id client invalid!\n'

        try:
            srv.adauga_client(id_client, nume, -cnp)
            assert False
        except ValidError as ve:
            assert str(ve) == 'cnp invalid!\n'

    def __ruleaza_teste_service(self):
        self.__ruleaza_teste_service_filme()
        self.__ruleaza_teste_service_clienti()

    def ruleaza_teste(self):
        #metoda (functie) care apeleaza pentru un obiect din clasa Teste metodele private ruleaza_teste_domeniu() si ruleaza_teste_validare
        #testarea tuturor metodelor (functiilor) se face folosind instructiunea assert

        self.__ruleaza_teste_domeniu()  #metoda care ruleaza teste pentru clasele din pachetul domeniu, modulul entitati
        self.__ruleaza_teste_validare() #metoda care ruleaza teste pentru clasele din pachetul domeniu, folosind clasele de obiecte ValidatorFilm si ValidatorClient din pachetul validare, modulul validatori
        self.__ruleaza_teste_repo()     #metoda care ruleaza teste pentru clasele din pachetul infrastructura, modulul repos
        self.__ruleaza_teste_service()  #metoda care ruleaza teste pentru clasele din pachetul service
