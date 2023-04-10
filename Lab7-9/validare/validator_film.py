#din modulul exceptii al pachetului erori importam clasa ValidError (obictele acestei clase vor fi de fapt obiecte de clasa Exception)
from erori.exceptii import ValidError

class ValidatorFilm:
    #clasa pe care o definim pentru a valida campurile (componentele) unui obiect de clasa Film

    def valideaza(self, film_rau):
        #metoda corespunzatoare unui obiect de clasa ValidatorFilm care valideaza pe rand fiecare din campurile obiectului de clasa Film: film_rau
        #date de intrare: film_rau - obiect de clasa Film pe care dorim sa il validam
        #date de iesire: nimic - daca filmul film_rau este valid (fiecare camp al acestui obiect de clasa Film respecta restrictiile impuse asupra campului respectiv)
        #                eroare de tipul ValidError (Exception) cu mesajul err - daca cel putin un camp al filmului film_rau nu este valid (prin urmare obiectul film_rau de clasa Film va fi la randul lui invalid)

        err = '' #lista de erori (sir de caractere/string)
        if film_rau.get_id_film() < 0: #campul id_film al unui obiect de clasa Film este un numar natural
            #campul id_film al filmului film_rau este invalid
            err += 'id film invalid!\n' #updatam lista de erori prin concatenarea noii erori gasite la stringul err
        if film_rau.get_titlu() == '': #campul titlu al unui obiect de clasa Film este un string (sir de caractere) nevid
            #campul titlu al filmului film_rau este invalid
            err += 'titlu invalid!\n' #updatam lista de erori prin concatenarea noii erori gasite la stringul err
        if film_rau.get_descriere() == '': #campul descriere al unui obiect de clasa Film este un string (sir de caractere) nevid
            #campul descriere al filmului film_rau este invalid
            err += 'descriere invalida!\n' #updatam lista de erori prin concatenarea noii erori gasite la stringul err
        if film_rau.get_gen() == '': #campul gen al unui obiect de clasa Film este un string (sir de caractere) nevid
            #campul gen al filmului film_rau este invalid
            err += 'gen invalid!\n' #updatam lista de erori prin concatenarea noii erori gasite la stringul err
        if film_rau.get_an_lansare() < 1897 or film_rau.get_an_lansare() > 2020: #campul an_lansare al unui obiect de clasa Film este un numar intreg cuprins in intervalul [1897, 2020]
            #campul an_lansare al filmului film_rau este invalid
            err += 'an de lansare invalid!\n' #updatam lista de erori prin concatenarea noii erori gasite la stringul err
        if film_rau.get_durata() < 60 or film_rau.get_durata() > 210: #campul durata a unui obiect de clasa Film este un numar intreg cuprins in intervalul [60, 210]
            #campul durata al filmului film_rau este invalid
            err += 'durata totala de rulare invalida!\n' #updatam lista de erori prin concatenarea noii erori gasite la stringul err
        if len(err): #am gasit cel putin un camp invalid al obiectului de clasa Film (lista de erori este nevida)
            raise ValidError(str(err)) #ridicam o eroare de tipul ValidError cu mesajul err (lista de erori)