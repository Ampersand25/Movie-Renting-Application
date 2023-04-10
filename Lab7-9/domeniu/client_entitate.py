class Client:
    #clasa care defineste un obiect cu urmatoarele informatii incapsulate (private):
    #campuri (proprietati): id_client, nume, cnp
    #metode (comportamente): getters (pentru a accesa campurile id_client, nume si cnp ale unui obiect de clasa Client din afara clasei)
    #                        setter (pentru a modifica campul nume al unui obiect de clasa Client din afara clasei)
    #                        __eq__ (suprascriem metoda __eq__ pentru a compara doua obiecte de clasa Client dupa campul id_client, ci nu dupa adresa din memorie a obiectelor respective)
    #                        str (suprascriem metoda str pentru a converti un obiect de clasa Client la un string in care vom avea pe cate o linie stringul corespunzator fiecarui camp al obiectului)

    #self refera obiectul de clasa Client pentru care s-a apelat una din metodele (functiile) de mai jos

    def __init__(self, id_client, nume, cnp):
        #metoda (constructor) care ne initializeaza un obiect de clasa Client (populeaza campurile obiectului cu parametrii de intrare ai metodei)
        #date de intrare: id_client - numar intreg
        #                 nume      - string (sir de caractere) nevid
        #                 cnp       - numar intreg cu exact 13 cifre
        #date de iesire: -

        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        #metoda getter pentru a accesa id-ul unui client din exteriorul clasei Client (campul __id_client este privat <=> poate fi accesat doar din interiorul clasei Client)
        #date de intrare: -
        #date de iesire: id-ul (identificatorul unic) clientului - numar natural (intreg fara semn)

        return self.__id_client

    def get_nume(self):
        #metoda getter pentru a accesa numele unui client din exteriorul clasei Client (campul __nume este privat <=> poate fi accesat doar din interiorul clasei Client)
        #date de intrare: -
        #date de iesire: numele complet al clientului (nume + prenume) - string (sir de caractere) nevid

        return self.__nume

    def set_nume(self, nume_nou):
        #metoda de tip setter care modifica campul privat nume al unui obiect de clasa Client
        #functia inlocuieste numele curent din campul nume al clientului cu stringul nume_nou
        #date de intrare: nume_nou - sir de caractere (str) nevid
        #date de iesire: - (nimic)

        self.__nume = nume_nou

    def set_cnp(self, cnp_nou):
        #metoda de tip setter care modifica campul privat cnp al unui obiect de clasa Client
        #functia inlocuieste cnp-ul curent din campul cnp al clientului cu stringul cnp_nou
        #date de intrare: cnp_nou - numar natural de 13 cifre (cuprins in intervalul [1000000000000, 9999999999999] = [1e+12, 1e+13))
        #date de iesire: - (nimic)

        self.__cnp = cnp_nou

    def get_cnp(self):
        #metoda getter pentru a accesa cnp-ul unui client din exteriorul clasei Client (campul __cnp este privat <=> poate fi accesat doar din interiorul clasei Client)
        #date de intrare: -
        #date de iesire: codul numeric personal (cnp-ul) clientului - numar natural de 13 cifre (cuprins in intervalul [1000000000000, 9999999999999] = [1e+12, 1e+13))

        return self.__cnp

    def __str__(self):
        #metoda care returneaza un string (sir de caractere) care sa contina fiecare camp al obiectului de clasa Client pentru care apelam metoda, convertit la str si urmat de linie noua (caracterul '\n')
        #date de intrare: -
        #date de iesire: str - string (sir de caractere) corespunzator obiectului de clasa Client

        return 'id: ' + str(self.__id_client) + '\nnume: ' + self.__nume + '\ncnp: ' + str(self.__cnp) + '\n'

    def __eq__(self, other):
        #metoda care compara doua obiecte de clasa Client: self (obiectul de clasa pentru care apelam metoda) si other (parametrul de intrare al metodei) din punct de vedere al campului/componentei id_client
        #date de intrare: other - un obiect de clasa Client cu care vrem sa comparam obiectul pe care apelam metoda
        #date de iesire: False - daca cele doua obiecte nu au aceleasi valoari in campurile id_client si cnp (cele doua obiecte refera clienti diferite)
        #                True - daca cele doua obiecte au aceeasi valoare in campul id_client sau in campul cnp (cele doua obiecte refera de fapt acelasi client, nu pot exista doi clienti diferiti cu acelasi id_client sau doua persoane cu acelasi cnp <=> id_client si cnp sunt doi identificatori unici)

        return self.__id_client == other.__id_client or self.__cnp == other.__cnp