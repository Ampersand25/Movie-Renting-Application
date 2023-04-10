class ValidError(Exception):
    #clasa care defineste un obiect de clasa ValidError ca si o exceptie Exception
    #astfel obiectul de clasa ValidError va fi o exceptie de tipul Exception (cele doua obiecte sunt de fapt acelasi obiect)
    #in acest caz, instructiunile: raise ValidError si raise Exception vor fi echivalente

    pass #clasa vida (nu contine nicio metoda/functie si prin urmare obiectele de clasa ValidError nu vor avea campuri/componente)

class RepoError(Exception):
    #clasa care defineste un obiect de clasa RepoError ca si o exceptie Exception
    #astfel obiectul de clasa RepoError va fi o exceptie de tipul Exception (cele doua obiecte sunt de fapt acelasi obiect)
    #in acest caz, instructiunile: raise RepoError si raise Exception vor fi echivalente

    pass #clasa vida (nu contine nicio metoda/functie si prin urmare obiectele de clasa RepoError nu vor avea campuri/componente)