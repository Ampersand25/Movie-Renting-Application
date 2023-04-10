'''
Enunt problema:

P3. Închiriere filme

Scrieți o aplicație pentru o firmă de închiriere de filme.
Aplicația stochează:
    - filme: <id>,<titlu>,<descriere>,<gen>,etc
    - clienți: <id>, <nume>, <CNP>,etc
Creați o aplicație care permite:
    - gestiunea listei de filme și clienți.
    - adaugă, șterge, modifică, lista de filme, lista de clienți
    - căutare film, căutare clienți.
    - Închiriere/returnare filme
    - Rapoarte:
        > Clienți cu filme închiriate ordonat dupa: nume, după numărul de filme închiriate
        > Cele mai inchiriate filme.
        > Primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)
'''

#importam clasa Teste din modulul teste al pachetului testare
from testare.teste import Teste

#importam clasele ValidatorFilm, ValidatorClient si ValidatorInchiriere din modulul validatori al pachetului validare
from validare.validator_film import ValidatorFilm
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere

#importam clasele RepositoryFilme, RepositoryClienti si RepositoryInchirieri din modulul repos al pachetului infrastructura
from infrastructura.repo_filme import RepositoryFilme
from infrastructura.repo_clienti import RepositoryClienti
from infrastructura.repo_inchirieri import RepositoryInchirieri

from infrastructura.file_repo_filme import FileRepositoryFilme
from infrastructura.file_repo_clienti import FileRepositoryClienti
from infrastructura.file_repo_inchirieri import FileRepositoryInchirieri

#importam clasele ServiceFilme, ServiceClienti si ServiceInchirieri din modulul servicii al pachetului business
from business.servicii_filme import ServiceFilme
from business.servicii_clienti import ServiceClienti
from business.servicii_inchirieri import ServiceInchirieri
from business.servicii_rapoarte import ServiceRapoarte

#importam clasa UI (User Interface) din modulul consola al pachetului prezentare
from prezentare.consola import UI
from prezentare.consola import LucruMemorieFisiere

import unittest

from testare.teste_domeniu import *
from testare.teste_validare import *
from testare.teste_infrastructura import *
from testare.teste_business import *

if __name__ == '__main__':
    #verificam daca numele modulului (fisierului py) curent este main

    #unittest.main()

    teste = Teste() #teste va fi un obiect de clasa Teste
    teste.ruleaza_teste() #apelam metoda ruleaza_teste() pentru obiectul teste de clasa Teste
                          #astfel rulam toate testele programului inainte de lansarea in executie a aplicatiei, pentru a detecta eventuale erori de implementare

    #cream validatori pentru cele trei entitati definite prin obiecte ale unor clase: film, client si inchiriere
    valid_film = ValidatorFilm()
    valid_client = ValidatorClient()
    valid_inchiriere = ValidatorInchiriere()

    lucreaza_memorie_fisiere = LucruMemorieFisiere()
    if lucreaza_memorie_fisiere.verifica_lucru_memorie():
        #cream cele trei obiecte de tip repository in care vom memora filmele (in obiectul repo_filme de clasa RepositoryFilme), clientii (in obiectul repo_clienti de clasa RepositoryClienti) precum si inchirierile (in obiectul repo_inchirieri de clasa RepositoryInchirieri) din aplicatie
        repo_filme = RepositoryFilme()
        repo_clienti = RepositoryClienti()
        repo_inchirieri = RepositoryInchirieri()

        #cream obiectele srv_filme de clasa ServiceFilme, srv_clienti de clasa ServiceClienti precum si srv_inchirieri de clasa ServiceInchirieri
        #obiectului srv_filme ii pasam ca si parametrii obiectele valid_film (validator pentru un obiect film de clasa Film) precum si repo_filme (repository-ul tuturor obiectelor film de clasa Film)
        #obiectului srv_clienti ii pasam ca si argumente obiectele valid_client (validator pentru un obiect client de clasa Client) precum si repo_clienti (repository-ul tuturor obiectelor client de clasa Client)
        #obiectului srv_inchirieri ii pasam ca si argumente obiectele srv_inchirieri (validator pentru un obiect inchiriere de clasa Inchiriere) precum si repository-urile celor 3 entitati (obiecte), ci anume repo_inchirieri (repository-ul in care vom retine toate inchirierile create), repo_filme (repository-ul in care vom retine toate filmele create) si repo_clienti (repository-ul in care vom retine toti clientii creati)
        srv_filme = ServiceFilme(valid_film, repo_filme, repo_inchirieri)
        srv_clienti = ServiceClienti(valid_client, repo_clienti, repo_inchirieri)
        srv_inchirieri = ServiceInchirieri(valid_inchiriere, repo_inchirieri, repo_filme, repo_clienti)
        srv_rapoarte = ServiceRapoarte(repo_inchirieri)
    else:
        filename_filme = 'filme.txt'
        filename_clienti = 'clienti.txt'
        filename_inchirieri = 'inchirieri.txt'

        file_repo_filme = FileRepositoryFilme(filename_filme)
        file_repo_clienti = FileRepositoryClienti(filename_clienti)
        file_repo_inchirieri = FileRepositoryInchirieri(filename_inchirieri)

        srv_filme = ServiceFilme(valid_film, file_repo_filme, file_repo_inchirieri)
        srv_clienti = ServiceClienti(valid_client, file_repo_clienti, file_repo_inchirieri)
        srv_inchirieri = ServiceInchirieri(valid_inchiriere, file_repo_inchirieri, file_repo_filme, file_repo_clienti)
        srv_rapoarte = ServiceRapoarte(file_repo_inchirieri)

    #cream obiectul consola de clasa UI caruia ii parsam ca si argumente (parametrii) obiectele srv_filme (obiect de clasa ServiceFilme), srv_clieni (obiect de clasa ServiceClienti) si srv_inchirieri (obiect de clasa ServiceInchirieri) create anterior
    console = UI(srv_filme, srv_clienti, srv_inchirieri, srv_rapoarte)

    #lansam in rulare/executie aplicatia de tip consola cu interfata utilizator prin apelarea functiei/metodei run_app a obiectului console de clasa UI (User Interface)
    console.run_app()