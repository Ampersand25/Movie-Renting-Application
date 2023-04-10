#din modulul exceptii al pachetului erori importam clasa ValidError (obictele acestei clase vor fi de fapt obiecte de clasa Exception)
from erori.exceptii import ValidError

class ValidatorClient:
    #clasa pe care o definim pentru a valida campurile (componentele) unui obiect de clasa Client

    def valideaza(self, client_rau):
        #metoda corespunzatoare unui obiect de clasa ValidatorClient care valideaza pe rand fiecare din campurile obiectului de clasa Client: client_rau
        #date de intrare: client_rau - obiect de clasa Client pe care vrem sa il validam
        #date de iesire: nimic - daca clientul client_rau este valid (fiecare camp al acestui obiect de clasa Client respecta restrictiile impuse asupra campului respectiv)
        #                eroare de tipul ValidError (Exception) cu mesajul err - daca cel putin un camp al clientului client_rau nu este valid (prin urmare obiectul client_rau de clasa Client va fi la randul lui invalid)

        err = '' #lista de erori (reprezentata printr-un sir de caractere care va contine concatenarea stringurilor corespunzatore mesajelor tuturor erorilor gasite)
        if client_rau.get_id_client() < 0: #campul id_client al unui obiect de clasa Client este un intreg cu semn (>= 0)
            #campul id_client al clientului client_rau este invalid
            err += 'id client invalid!\n' #adaugam mesajul de eroare 'id client invalid!\n' la lista de erori err (str) prin concatenarea celor doua siruri de caractere
        if client_rau.get_nume() == '': #campul nume al unui obiect de clasa Client este un string (sir de caractere) nevid
            #campul nume al clientului client_rau este invalid
            err += 'nume invalid!\n' #adaugam mesajul de eroare 'nume invalid!\n' la lista de erori err (str) prin concatenarea celor doua siruri de caractere
        if client_rau.get_cnp() < 1e+12 or client_rau.get_cnp() >= 1e+13: #campul cnp al unui obiect de clasa Client este un numar intreg care contine cu exactitate 13 cifre (numar intreg din intervalul [1e+12, 1e+13))
            #campul cnp al clientului client_rau este invalid
            err += 'cnp invalid!\n' #adaugam mesajul de eroare 'cnp invalid!\n' la lista de erori err (str) prin concatenarea celor doua siruri de caractere
        if len(err): #am gasit cel putin un camp invalid al obiectului de clasa Client (lista de erori este nevida)
            raise ValidError(str(err)) #ridicam o eroare de tipul ValidError cu mesajul err (lista de erori)