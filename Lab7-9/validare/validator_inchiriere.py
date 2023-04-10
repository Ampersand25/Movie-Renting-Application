#din modulul exceptii al pachetului erori importam clasa ValidError (obictele acestei clase vor fi de fapt obiecte de clasa Exception)
from erori.exceptii import ValidError
import datetime

class ValidatorInchiriere:
    #clasa pe care o definim pentru a valida campurile (componentele) unui obiect de clasa Inchiriere

    def __valideaza_an_bisect(self, an_curent):
        #metoda privata care verifica daca un an dat ca si argument/parametru este sau nu bisect
        #date de intrare: an_curent - un an (numar intreg fara semn (unsigned)) care indica anul curent
        #date de iesire: True  - anul an_curent este bisect
        #                False - anul an_curent nu este bisect

        if ((an_curent % 4 == 0) and (an_curent % 100 != 0)):
            return True
        if (an_curent % 400 == 0):
            return True
        return False

    def __zile_luni_an_curent(self, an_curent):
        #metoda privata care returneaza o mapare (structura de date de tip map) a lunilor (chei) la numarul de zile corespunzator (valori numerice ale cheilor)
        #date de intrare: an_curent - anul curent
        #date de iesire: map care contine pentru fiecare luna din an (indexata de la 1 la 12, incepand cu luna februarie si terminand cu decembrie) numarul de zile

        if self.__valideaza_an_bisect(an_curent) == True: #verificam daca anul curent este sau nu bisect pentru a determina numarul de zile din luna februarie
            an_bisect = 1 #anul curent este bisect (februarie are 29 de zile)
        else:
            an_bisect = 0 #anul curent nu este bisect (februarie are 28 de zile)

        #returnam un map care pentru fiecare luna din an contine numarul de zile din luna respectiva
        return {1 : 31,               #luna ianuarie (1) contine 31 de zile
                2 : (28 + an_bisect), #luna februarie (2) contine 28 de zile daca anul curent nu este bisect si 29 daca este
                3 : 31,               #luna martie (3) contine 31 de zile
                4 : 30,               #luna aprilie (4) contine 30 de zile
                5 : 31,               #luna mai (5) contine 31 de zile
                6 : 30,               #luna iunie (6) contine 30 de zile
                7 : 31,               #luna iulie (7) contine 31 de zile
                8 : 31,               #luna august (8) contine 31 de zile
                9 : 30,               #luna septembrie (9) contine 30 de zile
                10: 31,               #luna octombrie (10) contine 31 de zile
                11: 30,               #luna noiembrie (11) contine 30 de zile
                12: 31}               #luna decembrie (12) contine 31 de zile

    def __valideaza_termen_predare(self, data_rea):
        #metoda privata care valideaza daca o data pasata ca si parametru/argument la apelul metodei/functiei poate sa fie un termen de predare pentru un film (adica daca data este in viitor, cel mai devreme maine fata de momentul inchirierii filmului)
        #date de intrare: data_rea - un obiect de clasa Data
        #date de iesire: err - lista de erori (daca este vida => data data_rea este valida, in caz contrar (len(err) != 0 <=> lista de erori nu e vida) data_rea nu reprezinta o data valida)

        data_curenta = datetime.datetime.now() #data curenta
        zi_curenta = data_curenta.day #ziua curenta
        luna_curenta = data_curenta.month #luna curenta
        an_curent = data_curenta.year #anul curent

        err = '' #lista de erori (sir de caractere)

        if data_rea.get_an() < an_curent:
            err += 'termen de predare invalid!\n' #adaugam eroare la lista de erori
        elif data_rea.get_an() == an_curent:
            if data_rea.get_luna() < luna_curenta:
                err += 'termen de predare invalid!\n' #adaugam eroare la lista de erori
            elif data_rea.get_luna() == luna_curenta:
                if data_rea.get_zi() <= zi_curenta:
                    err += 'termen de predare invalid!\n' #adaugam eroare la lista de erori

        return err #returnam lista de erori

    #clasa pe care o definim pentru a valida campurile (componentele) unui obiect de clasa Data (adica atributele zi, luna si an)
    def __valideaza_data(self, data_rea):
        #metoda privata care valideaza o data calendaristica data_rea (verifica ca valorile din campurile/atributele zi, luna si an sa fie valori valide)
        #date de intrare: data_rea - data calendaristica (obiect de clasa Data)
        #date de iesire: err - lista (sir de caractere sau string) de erori

        zile_luna = self.__zile_luni_an_curent(data_rea.get_an()) #map care contine ca si chei numarul tuturor lunilor din an si ca si valori numarul de zile al acestora

        err = '' #lista de erori care este initial vida (nu s-au gasit erori inca)

        if data_rea.get_zi() < 1 or ((data_rea.get_luna() >= 1 and data_rea.get_luna() <= 12) and data_rea.get_zi() > zile_luna[data_rea.get_luna()]):
            err += 'zi invalida!\n'
        if data_rea.get_luna() < 1 or data_rea.get_luna() > 12:
            if not len(err):
                err += 'zi invalida!\n'
            err += 'luna invalida!\n'
        if data_rea.get_an() < 1:
            err += 'an invalid!\n'

        if len(err): #s-a detectat cel putin un camp/atribut invalid pentru data calendaristica primita de metoda/fuctia curenta ca si parametru
            return err #returnam lista de erori

        return self.__valideaza_termen_predare(data_rea) #verificam daca data calendaristica data_rea (validata cu succes) poate sa reprezinte un termen de returnare (retur) a unui film

    #clasa pe care o definim pentru a valida campurile (componentele) unui obiect de clasa Inchiriere
    def valideaza(self, inchiriere_rea):
        #metoda corespunzatoare unui obiect de clasa ValidatorInchiriere care valideaza campurile unui obiect de clasa Inchiriere
        #date de intrare: inchiriere_rea - obiect de clasa Inchiriere pe care dorim sa il validam
        #date de iesire: nimic - daca inchirierea inchiriere_rea este valida (fiecare camp al acestui obiect de clasa Inchiriere respecta restrictiile impuse asupra campului respectiv)
        #                eroare de tipul ValidError (Exception) cu mesajul err - daca cel putin un camp al inchirierii inchiriere_rea nu este valid (prin urmare obiectul inchiriere_rea de clasa Inchiriere va fi la randul lui invalid)

        err = ''  #lista de erori (sir de caractere/string)

        if inchiriere_rea.get_id_inchiriere() < 0: #campul id_inchiriere al unui obiect de clasa Inchiriere este un numar natural
            #campul id_inchiriere al inchirierii inchiriere_rea este invalid
            err += 'id inchiriere invalid!\n' #adaugam eroarea gasita la lista de erori (sir de caractere/string)

        err += self.__valideaza_data(inchiriere_rea.get_data()) #validam data din campul data a unui obiect de clasa inchiriere (inchiriere_rea) apeland metoda privata __valideaza_data() avand ca parametru data pe care vrem sa o validam

        if len(err): #cel putin un camp/atribut al obiectului de clasa Inchiriere inchiriere_rea este invalid => inchirierea inchiriere_rea este invalida
            raise ValidError(str(err)) #raise Exception(str(err))
                                       #aruncam o eroare de tipul ValidError (Exception) cu mesajul err (string)