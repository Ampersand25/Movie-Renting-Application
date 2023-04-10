class Inchiriere:
    def __init__(self, id_inchiriere, film, client, data):
        #metoda (constructor) care ne initializeaza un obiect de clasa Client (populeaza campurile obiectului cu parametrii de intrare ai metodei)
        #date de intrare: id_inchiriere - numar intreg
        #                 film          - obiect de clasa Film (filmul pe care clientul client doreste sa il inchirieze)
        #                 client        - obiect de clasa Client (clientul care vrea sa inchirieze filmul din campul/atributul film)
        #                 data          - obiect de clasa Data (reprezinta o data calendaristica care indica termenul limita de predare a filmului film de catre clientul client)
        #date de iesire: -

        self.__id_inchiriere = id_inchiriere
        self.__film = film
        self.__client = client
        self.__data = data

    def get_id_inchiriere(self):
        #metoda getter pentru a accesa id-ul unei inchirieri din exteriorul clasei Inchiriere (campul __id_inchiriere este privat <=> poate fi accesat doar din interiorul clasei Inchiriere)
        #date de intrare: -
        #date de iesire: id-ul (identificatorul unic) inchirierii - numar natural (intreg fara semn)

        return self.__id_inchiriere

    def get_film(self):
        #metoda getter pentru a accesa filmul dintr-o inchiriere din exteriorul clasei Inchiriere
        #date de intrare: -
        #date de iesire: filmul inchiriat - obiect de clasa Film

        return self.__film

    def set_film(self, film_nou):
        self.__film = film_nou

    def get_client(self):
        #metoda getter pentru a accesa clientul dintr-o inchiriere din exteriorul clasei Inchiriere
        #date de intrare: -
        #date de iesire: clientul care a inchiriat (vrea sa inchirieze) un film - obiect de clasa Client

        return self.__client

    def set_client(self, client_nou):
        self.__client = client_nou

    def get_data(self):
        #metoda getter pentru a accesa data (termenul de retur a unui film) dintr-o inchiriere din exteriorul clasei Inchiriere
        #date de intrare: -
        #date de iesire: data de returnare a filmului (termenul limita) - obiect de clasa Data (reprezinta o data calendaristica cu zi, luna si an)

        return self.__data

    def set_data(self, data_noua):
        self.__data = data_noua

    def __str__(self):
        #metoda care returneaza un string (sir de caractere) care sa contina fiecare camp al obiectului de clasa Inchiriere pentru care apelam metoda, convertit la str si urmat de linie noua (caracterul '\n')
        #date de intrare: -
        #date de iesire: str - string (sir de caractere) corespunzator obiectului de clasa Inchiriere

        return 'id inchiriere: ' + str(self.__id_inchiriere) + '\n\nclient:\n' + str(self.__client) + '\nfilm:\n' + str(self.__film) + '\ntermen returnare film:\n' + str(self.__data) + '\n'

    def __eq__(self, other):
        #metoda care compara doua obiecte de clasa Inchiriere: self (obiectul de clasa pentru care apelam metoda) si other (parametrul de intrare al metodei) din punct de vedere al campului/componentei id_inchiriere
        #date de intrare: other - un obiect de clasa Inchiriere cu care vrem sa comparam obiectul pe care apelam metoda
        #date de iesire: False - daca cele doua obiecte nu au aceleasi valoari in campurile id_inchiriere
        #                True - daca cele doua obiecte au aceeasi valoare in campul id_inchiriere

        return self.__id_inchiriere == other.__id_inchiriere