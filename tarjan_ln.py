def czy_ma_cykle(graf,wierzcholek,kolory):
    kolory[wierzcholek]="szary"

    for i in graf[wierzcholek]:
        if kolory[i] == "szary":return True
        if czy_ma_cykle(graf,i,kolory.copy()): return True
    return False

def Tarjan_ln(graf,wierzcholek = None,kolory=None,L=None):
    if L == None : L=[]
    A = len(graf)
    flaga = True
    if kolory == None :
        kolory = ["bialy"]*(A+1)
        flaga = False
    
#ustalanie wierzcholka od ktorego zaczniemy sortowanie jezeli nie zostal podany
    if wierzcholek == None :
        flaga = False
        stopnie_wierzcholkow=[0]*(A+1)
        for i in range(1,A+1):
            for j in graf[i]:
                stopnie_wierzcholkow[j]+=1
        for i in range(1,A):
            if stopnie_wierzcholkow[i] == 0 and kolory[i] == "bialy":
                wierzcholek = i
                break
        if wierzcholek == None :
            return 
        
    if czy_ma_cykle(graf,wierzcholek,kolory.copy()):
        return 

#algorytm sortowania topologicznego 
    kolory[wierzcholek] = "szary"
    for i in graf[wierzcholek]:
        if kolory[i] ==  "bialy":
            L,kolory=Tarjan_ln(graf,i,kolory,L)
    kolory[wierzcholek]="czarny"
    L.append(wierzcholek)
    if flaga:
        return [L,kolory]
    if "bialy" in kolory[1:]:
        return Tarjan_ln(graf,None,kolory,L)
    return L[::-1]

def test_tarjan_ln(f):
    from representation import lista_nastepnikow
    poczatkowy = input("Podaj wierzchołek początkowy: ")
    poczatkowy = int(poczatkowy)  if poczatkowy.strip() != "" else None
    lista = lista_nastepnikow(f)
    wynik = Tarjan_ln(lista,poczatkowy)
    print(wynik if wynik is not None else "Graf zawiera cykl")



# TESTOWANIE FUNKCJI
if __name__ == "__main__":    
    with open(input("Plik: "), "r") as f:
        plik = f.readlines()

    test_tarjan_ln(plik)
