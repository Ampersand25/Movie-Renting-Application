from domeniu.inchiriere_entitate import Inchiriere
from domeniu.data_entitate import Data
from erori.exceptii import ValidError

#############################################
#Pentru functia/metoda adauga_inchirieri_repo
from domeniu.film_entitate import Film
from domeniu.client_entitate import Client
#############################################

class ServiceInchirieri:

    def __init__(self, validator_inchiriere, repo_inchirieri, repo_filme, repo_clienti):
        self.__validator_inchirieri = validator_inchiriere
        self.__repo_inchirieri = repo_inchirieri
        self.__repo_filme = repo_filme
        self.__repo_clienti = repo_clienti

    def inchiriere_film(self, id_inchiriere, id_film, id_client, data):
        film = self.__repo_filme.cauta_dupa_id(id_film)
        client = self.__repo_clienti.cauta_dupa_id(id_client)

        if len(data) != 3:
            raise Exception('numar invalid de argumente pentru data calendaristica!\n')

        zi = int(data[0])
        luna = int(data[1])
        an = int(data[2])
        termen_predare = Data(zi, luna, an)
        inchiriere_noua = Inchiriere(id_inchiriere, film, client, termen_predare)
        self.__validator_inchirieri.valideaza(inchiriere_noua)
        self.__repo_inchirieri.adauga(inchiriere_noua)

    def get_inchirieri(self):
        return self.__repo_inchirieri.get_all()

    def returnare_film(self, id_inchiriere):
        if id_inchiriere < 0:
            raise ValidError('id inchiriere invalid!\n')

        self.__repo_inchirieri.sterge_dupa_id(id_inchiriere)

    def modifica_inchiriere(self, id_inchiriere, id_film, id_client, data_noua):
        film = self.__repo_filme.cauta_dupa_id(id_film)
        client = self.__repo_clienti.cauta_dupa_id(id_client)

        if len(data_noua) != 3:
            raise Exception('numar invalid de argumente pentru data calendaristica!\n')

        zi = int(data_noua[0])
        luna = int(data_noua[1])
        an = int(data_noua[2])
        termen_predare_nou = Data(zi, luna, an)
        inchiriere_noua = Inchiriere(id_inchiriere, film, client, termen_predare_nou)
        self.__validator_inchirieri.valideaza(inchiriere_noua)
        self.__repo_inchirieri.modifica(inchiriere_noua)

    def cauta_inchiriere(self, id_inchiriere):
        if id_inchiriere < 0 :
            raise ValidError('id inchiriere invalid!\n')

        return self.__repo_inchirieri.cauta_dupa_id(id_inchiriere)

    def nr_inchirieri(self):
        return len(self.__repo_inchirieri)

    def adauga_inchirieri_repo(self):
        self.__repo_filme.adauga(Film(0, 'The Godfather', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 'police movie', 1972, 178))
        self.__repo_filme.adauga(Film(1, 'It', 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.', 'horror/thriller', 2017, 135))
        self.__repo_filme.adauga(Film(2, 'Tenet', 'Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.', 'action and SF', 2020, 150))
        self.__repo_filme.adauga(Film(3, 'The Gift', "A young married couple's lives are thrown into a harrowing tailspin when an acquaintance from the husband's past brings mysterious gifts and a horrifying secret to light after more than 20 years.", 'mistery/thriller/psychological', 2015, 108))
        self.__repo_filme.adauga(Film(4, 'The Lord of the Rings: The Fellowship of the Ring', 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.', 'action/adventure/drama', 2001, 178))
        self.__repo_filme.adauga(Film(5, 'Avatar', 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', 'fantasy/action/adventure', 2009, 162))
        self.__repo_filme.adauga(Film(6, 'The Matrix', 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.', 'action', 1999, 136))
        self.__repo_filme.adauga(Film(7, 'Beauty and the Beast', 'A selfish Prince is cursed to become a monster for the rest of his life, unless he learns to fall in love with a beautiful young woman he keeps prisoner.', 'fantasy/musical', 2017, 129))
        self.__repo_filme.adauga(Film(8, 'Toy Story', "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", 'animation/adventure/comedy', 1995, 81))
        self.__repo_filme.adauga(Film(9, 'Psycho', "A Phoenix secretary embezzles $40,000 from her employer's client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.", 'horror', 1960, 109))

        self.__repo_clienti.adauga(Client(0, 'Radu Florian Sava', 3683275286429))
        self.__repo_clienti.adauga(Client(1, 'Dragos Spiridon', 8626931422363))
        self.__repo_clienti.adauga(Client(2, 'Mihai Popescu', 9473816439262))
        self.__repo_clienti.adauga(Client(3, 'Robert Andrei Iowa Pruteanu', 2682164926429))
        self.__repo_clienti.adauga(Client(4, 'Norbert Roszinecz', 6933632158421))
        self.__repo_clienti.adauga(Client(5, 'Ion Alexandru Anton', 5839154825932))
        self.__repo_clienti.adauga(Client(6, 'Alex Harry Poker Stan', 3849216539263))
        self.__repo_clienti.adauga(Client(7, 'Marius Sterian', 9423812892141))
        self.__repo_clienti.adauga(Client(8, 'Sebastian Raoul Sipos', 8639159642853))
        self.__repo_clienti.adauga(Client(9, 'Cristi Moldovan', 1853726839242))

        self.__repo_inchirieri.adauga(Inchiriere(0, self.__repo_filme.cauta_dupa_id(4), self.__repo_clienti.cauta_dupa_id(8), Data(26, 4, 2021)))
        self.__repo_inchirieri.adauga(Inchiriere(1, self.__repo_filme.cauta_dupa_id(7), self.__repo_clienti.cauta_dupa_id(3), Data(5, 8, 2025)))
        self.__repo_inchirieri.adauga(Inchiriere(2, self.__repo_filme.cauta_dupa_id(2), self.__repo_clienti.cauta_dupa_id(5), Data(15, 3, 2029)))
        self.__repo_inchirieri.adauga(Inchiriere(3, self.__repo_filme.cauta_dupa_id(9), self.__repo_clienti.cauta_dupa_id(8), Data(19, 12, 2020)))
        self.__repo_inchirieri.adauga(Inchiriere(4, self.__repo_filme.cauta_dupa_id(3), self.__repo_clienti.cauta_dupa_id(1), Data(23, 3, 2021)))
        self.__repo_inchirieri.adauga(Inchiriere(5, self.__repo_filme.cauta_dupa_id(1), self.__repo_clienti.cauta_dupa_id(4), Data(1, 9, 2024)))
        self.__repo_inchirieri.adauga(Inchiriere(6, self.__repo_filme.cauta_dupa_id(2), self.__repo_clienti.cauta_dupa_id(9), Data(8, 11, 2029)))
        self.__repo_inchirieri.adauga(Inchiriere(7, self.__repo_filme.cauta_dupa_id(4), self.__repo_clienti.cauta_dupa_id(3), Data(30, 1, 2022)))
        self.__repo_inchirieri.adauga(Inchiriere(8, self.__repo_filme.cauta_dupa_id(9), self.__repo_clienti.cauta_dupa_id(1), Data(18, 3, 2027)))
        self.__repo_inchirieri.adauga(Inchiriere(9, self.__repo_filme.cauta_dupa_id(0), self.__repo_clienti.cauta_dupa_id(8), Data(28, 11, 2021)))
        self.__repo_inchirieri.adauga(Inchiriere(10, self.__repo_filme.cauta_dupa_id(5), self.__repo_clienti.cauta_dupa_id(0), Data(30, 4, 2028)))