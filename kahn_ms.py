def kahn_ms(graf):
    A = len(graf)
    czy_wierzcholek_jest_usuniety = [0]*A
    L=[]*(A+1)

    while 0 in czy_wierzcholek_jest_usuniety:
        #ustalanie stopniow wierzcholkow
        stopnie_wiercholkow=[0]*len(graf)
        for i in range(A):
            for j in range(A):
                if graf[i][j] == -1 and czy_wierzcholek_jest_usuniety[j] == 0:
                    stopnie_wiercholkow[i]+=1

        #ustwiamy flaga ktora sprawdza nam czy ciag ma cykle
        czy_cykl = True

        #usuwanie wierzcholka o stopniu 0
        for i in range(A):
            if stopnie_wiercholkow[i] == 0 and czy_wierzcholek_jest_usuniety[i] == 0 : 
                L.append(i+1)
                czy_wierzcholek_jest_usuniety[i] = 1
                czy_cykl = False
        if czy_cykl : return 
    return L            
            
        

def test_kahn_ms(f):
    from representation import macierz_sasiedztwa

    macierz = macierz_sasiedztwa(f)
    wynik = kahn_ms(macierz)
    
    print(wynik if wynik is not None else "Graf zawiera cykl")

# TESTOWANIE FUNKCJI
if __name__ == "__main__":    
    with open(input("Plik: "), "r") as f:
        plik = f.readlines()

    test_kahn_ms(plik)

