#SORTARI
def for_key(element, key):
    return key(element)

#MergeSort - sortare prin interclasare
def merge(list, st, mij, dr, key, cmp, reverse):
    #functie de interclasare a jumatatilor dintr-un sir list: [st, mij] si [mij + 1, dr]
    #date de intrare: list - lista a caror jumatati dorim sa le interclasam
    #                 st   - indicele de inceput al primului subsir (a primei jumatati)
    #                 dr   - indicele de sfarsit al
    #                 mij  - (st + dr) / 2 - mijlocul intervalului [st, dr]
    #date de iesire: sirul list sortat pe intervalul [st, dr]

    i, j = st, mij + 1
    new_list = []
    while i <= mij or j <= dr:
        #if j > dr or (i <= mij and ((reverse == True and cmp(for_key(list[j], key), for_key(list[i], key))) or (reverse == False and cmp(for_key(list[i], key), for_key(list[j], key))))):
        if reverse == False:
            if j > dr or (i <= mij and cmp(for_key(list[i], key), for_key(list[j], key))):
                new_list.append(list[i])
                i += 1
            else:
                new_list.append(list[j])
                j += 1
        else:
            if i > mij or (j <= dr and cmp(for_key(list[i], key), for_key(list[j], key))):
                new_list.append(list[j])
                j += 1
            else:
                new_list.append(list[i])
                i += 1

    for idx in range(st, dr + 1):
        list[idx] = new_list[idx - st]

    '''
    k = 0
    for idx in range(st, dr + 1):
        list[idx] = new_list[k]
        k += 1
    '''

def merge_sort(list, st, dr, key, cmp, reverse):
    #algoritm care sorteaza o lista list de obiecte oarecare
    #date de intrare: list    - lista care se doreste a fi sortata
    #                 key     - campul/componenta dupa care se face sortarea (comparatia)
    #                 cmp     - criteriul de sortare
    #                 reverse - cum sa fie sortata lista (crescator/descrescator)
    #date de iesire: o permutare a listei list sortata dupa criteriul de comparatie cmp care compara campurile key a unor obiecte din lista list

    #base case
    if st >= dr: #if st >= dr:
        return
    #inductive step
    #divide
    mij = st + (dr - st) // 2
    merge_sort(list, st, mij, key, cmp, reverse)
    merge_sort(list, mij + 1, dr, key, cmp, reverse)
    #conquer
    merge(list, st, mij, dr, key, cmp, reverse)

    '''
    if st != dr: #if st < dr:
        #divide
        mij = st + (dr - st) // 2
        merge_sort(list, st, mij, key, cmp, reverse)
        merge_sort(list, mij + 1, dr, key, cmp, reverse)
        #conquer
        merge(list, st, mij, dr, key, cmp, reverse)
    '''

def merge_sort_func(list, key=lambda x:x, cmp=lambda x, y: x > y, reverse=False):
    merge_sort(list, 0, len(list) - 1, key, cmp, reverse)

#BingoSort
def bingo_sort(list, key, cmp, reverse):
    #algoritm care sorteaza o lista list de obiecte oarecare
    #date de intrare: list    - lista care se doreste a fi sortata
    #                 key     - campul/componenta dupa care se face sortarea (comparatia)
    #                 cmp     - criteriul de sortare
    #                 reverse - cum sa fie sortata lista (crescator/descrescator)
    #date de iesire: o permutare a listei list sortata dupa criteriul de comparatie cmp care compara campurile key a unor obiecte din lista list

    i = 0
    while i + 1 < len(list):  #while i < len(list) - 1
        minim = list[i]
        for j in range(i + 1, len(list)):
            if reverse == False:
                if cmp(for_key(list[j], key), for_key(minim, key)):
                    minim = list[j]
            else:
                if cmp(for_key(minim, key), for_key(list[j], key)):
                    minim = list[j]
        for j in range(i, len(list)):
            if for_key(list[j], key) == for_key(minim, key):
                '''
                aux = list[i]
                list[i] = list[j]
                list[j] = aux
                '''

                list[i], list[j] = list[j], list[i]
                i += 1

def bingo_sort_func(list, key=lambda x:x, cmp=lambda x, y: x > y, reverse=False):
    bingo_sort(list, key, cmp, reverse)