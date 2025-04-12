from collections import deque

def tarjan_ms(macierz_sasiedztwa, wierzcholek_poczatkowy=None):
    n = len(macierz_sasiedztwa)

    kolor = [0] * n  # 0: biały, 1: szary, 2: czarny
    result = deque()
    has_cycle = False

    def dfs(v):
        nonlocal has_cycle
        kolor[v] = 1  # szary
        for sasiad in range(n):
            if macierz_sasiedztwa[v][sasiad] == 1:
                if kolor[sasiad] == 1:  # szary -> cykl!
                    has_cycle = True
                    return
                elif kolor[sasiad] == 0:
                    dfs(sasiad)
                    if has_cycle: 
                        return
        kolor[v] = 2
        result.appendleft(v)


    # STARTOWANIE OD UŻYTKOWNIKA LUB DOMYŚLNEGO
    if wierzcholek_poczatkowy is not None:
        if 0 <= wierzcholek_poczatkowy < n:
            if kolor[wierzcholek_poczatkowy] == 0:
                dfs(wierzcholek_poczatkowy)
                if has_cycle:
                    return None
        else:
            print("Nieprawidłowy wierzchołek startowy.")
            return None
    else:
        # ZNAJDOWANIE STOPNI WEJŚCIOWYCH
        stopien = [0] * n
        for i in range(n):
            for j in range(n):
                if macierz_sasiedztwa[i][j] == 1:
                    stopien[j] += 1

        for v in range(n):
            if stopien[v] == 0 and kolor[v] == 0:
                dfs(v)
                if has_cycle:
                    return None

    # POZOSTAŁE BIAŁE WIERZCHOŁKI
    for v in range(n):
        if kolor[v] == 0:
            dfs(v)
            if has_cycle:
                return None

    return [i+1 for i in list(result)]


def test_tarjan_ms(f):
    from representation import macierz_sasiedztwa
    poczatkowy = input("Podaj wierzchołek początkowy: ")
    poczatkowy = int(poczatkowy) - 1 if poczatkowy.strip() != "" else None

    macierz = macierz_sasiedztwa(f)
    wynik = tarjan_ms(macierz, poczatkowy)
    
    print(wynik if wynik is not None else "Graf zawiera cykl")


# TESTOWANIE FUNKCJI
if __name__ == "__main__":    
    with open(input("Plik: "), "r") as f:
        plik = f.readlines()

    test_tarjan_ms(plik)
