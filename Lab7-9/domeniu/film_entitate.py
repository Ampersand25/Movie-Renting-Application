class Film:
    #clasa care defineste un obiect cu urmatoarele informatii incapsulate (private):
    #campuri (proprietati): id_film, titlu, descriere, gen, an_lansare, durata
    #metode (comportamente): getters (pentru a accesa campurile id_film, titlu, descriere, gen, an_lansare, durata ale unui obiect de clasa Film din afara clasei)
    #                        setters (pentru a modifica campurile titlu, descriere, gen, an_lansare, durata ale unui obiect de clasa Film din afara clasei)
    #                        __eq__ (suprascriem metoda __eq__ pentru a compara doua obiecte de clasa Film dupa campul id_film, ci nu dupa adresa din memorie a obiectelor respective)
    #                        str (suprascriem metoda str pentru a converti un obiect de clasa Film la un string in care vom avea pe cate o linie stringul corespunzator fiecarui camp al obiectului)

    #self refera obiectul de clasa Film pentru care s-a apelat una din metodele (functiile) de mai jos

    def __init__(self, id_film, titlu, descriere, gen, an_lansare, durata):
        #metoda (constructor) care ne initializeaza un obiect de clasa Film (populeaza campurile obiectului cu parametrii de intrare ai metodei)
        #date de intrare: id_film    - numar natural
        #                 titlu (numele filmului)                                         - str
        #                 descriere (o scurta prezentare a plot-ului filmului)            - str
        #                 gen (categoria in care se incadreaza filmul)                    - str
        #                 an_lansare (anul in care filmul a fost lansat in cinematografe) - numar natural din intervalul [1897, 2020]
        #                 durata (durata totala a filmului calculata in minute)           - numar natural din intervalul [60, 210]
        #date de iesire: -

        #campurile (componentele) clasei Film vor fi private (nu vor putea fi direct accesate si modificate din exteriorul clasei prin intermediul operatorului de calificare (.), doar cu ajutorul getterelor si al setterelor)
        #orice camp al unui obiect dintr-o clasa care incepe cu __ reprezinta un camp privat (acesta este incapsulat in clasa respectiva)
        self.__id_film = id_film
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        self.__an_lansare = an_lansare
        self.__durata = durata

    def get_id_film(self):
        #metoda getter pentru a accesa id-ul unui film din exteriorul clasei Film (campul __id_film este privat <=> poate fi accesat doar din interiorul clasei Film)
        #date de intrare: -
        #date de iesire: id-ul (identificatorul unic) filmului - numar natural (intreg fara semn)

        return self.__id_film

    def get_titlu(self):
        #metoda getter pentru a accesa titlul unui film din exteriorul clasei Film (campul __titlu este privat <=> poate fi accesat doar din interiorul clasei Film)
        #date de intrare: -
        #date de iesire: titlul filmului - string (sir de caractere) nevid (contine cel putin un caracter <=> lungimea sa este minim 1)

        return self.__titlu

    def set_titlu(self, titlu_nou):
        #metoda de tip setter care modifica campul privat titlu al unui obiect de clasa Film
        #functia inlocuieste titlul curent din campul titlu al filmului cu stringul titlu_nou
        #date de intrare: titlu_nou - sir de caractere (str) nevid
        #date de iesire: - (nimic)

        self.__titlu = titlu_nou

    def get_descriere(self):
        #metoda getter pentru a accesa descrierea unui film din exteriorul clasei Film (campul __descriere este privat <=> poate fi accesat doar din interiorul clasei Film)
        #date de intrare: -
        #date de iesire: descrierea filmului - string (sir de caractere) nevid

        return self.__descriere

    def set_descriere(self, descriere_noua):
        #metoda de tip setter care modifica campul privat descriere al unui obiect de clasa Film
        #functia inlocuieste descrierea curenta din campul descriere a filmului cu stringul descriere_noua
        #date de intrare: descriere_noua - sir de caractere (str) nevid
        #date de iesire: - (nimic)

        self.__descriere = descriere_noua

    def get_gen(self):
        #metoda getter pentru a accesa genul unui film din exteriorul clasei Film (campul __gen este privat <=> poate fi accesat doar din interiorul clasei Film)
        #date de intrare: -
        #date de iesire: genul filmului - string (sir de caractere) nevid

        return self.__gen

    def set_gen(self, gen_nou):
        #metoda de tip setter care modifica campul privat gen al unui obiect de clasa Film
        #functia inlocuieste genul curent din campul gen al filmului cu stringul gen_nou
        #date de intrare: gen_nou - sir de caractere (str) nevid
        #date de iesire: - (nimic)

        self.__gen = gen_nou

    def get_an_lansare(self):
        #metoda getter pentru a accesa anul de lansare a unui film din exteriorul clasei Film (campul __an_lansare este privat <=> poate fi accesat doar din interiorul clasei Film)
        #date de intrare: -
        #date de iesire: anul in care filmul a fost lansat - numar intreg fara semn (unsigned) din intervalul [1897, 2020] (primul film din istorie de minim o ora a fost lansat in anul 1897)

        return self.__an_lansare

    def set_an_lansare(self, an_lansare_nou):
        #metoda de tip setter care modifica campul privat an_lansare al unui obiect de clasa Film
        #functia inlocuieste anul de lansare curent din campul an_lansare al filmului cu intregul an_lansare
        #date de intrare: an_lansare_nou - intreg din intervalul [1897, 2020]
        #date de iesire: - (nimic)

        self.__an_lansare = an_lansare_nou

    def get_durata(self):
        #metoda getter pentru a accesa durata (timpul de rulare) a unui film din exteriorul clasei Film (campul __durata este privat <=> poate fi accesat doar din interiorul clasei Film)
        #date de intrare: -
        #date de iesire: durata filmului exprimata in minute - numar intreg din intervalul [60, 210] (consideram ca un film trebuie sa dureze minim (cel putin) o ora si maxim (cel mult) 3 ore si jumatate

        return self.__durata

    def set_durata(self, durata_noua):
        #metoda de tip setter care modifica campul privat durata al unui obiect de clasa Film
        #functia inlocuieste durata totala calculata in minute curenta din campul durata a filmului cu intregul durata_noua
        #date de intrare: durata_noua - intreg din intervalul [60, 210]
        #date de iesire: - (nimic)

        self.__durata = durata_noua

    def __str__(self):
        #metoda care returneaza un string (sir de caractere) care sa contina fiecare camp al obiectului de clasa Film pentru care apelam metoda, convertit la str si urmat de linie noua (caracterul '\n')
        #date de intrare: -
        #date de iesire: str - string (sir de caractere) corespunzator obiectului de clasa Film

        return 'id: ' + str(self.__id_film) + '\ntitlu: ' + self.__titlu + '\ndescriere: ' + self.__descriere + '\ngen: ' + self.__gen + '\nan lansare: ' + str(self.__an_lansare) + '\ndurata totala (minute): ' + str(self.__durata) + '\n'

    def __eq__(self, other):
        #metoda care compara doua obiecte de clasa Film: self (obiectul de clasa pentru care apelam metoda) si other (parametrul de intrare al metodei) din punct de vedere al campului/componentei id_film
        #date de intrare: other - un obiect de clasa Film cu care vrem sa comparam obiectul pe care apelam metoda
        #date de iesire: False - daca cele doua obiecte nu au aceeasi valoare in campul id_film (cele doua obiecte reprezinta filme diferite)
        #                True - daca cele doua obiecte au aceeasi valoare in campul id_film (cele doua obiecte reprezinta de fapt acelasi film, nu pot exista doua filme diferite cu acelasi id_film <=> id_film este un identificator unic)

        return self.__id_film == other.__id_film