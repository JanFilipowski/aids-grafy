def lista_nastepnikow(f):
    nastepniki = {}

    for k, line in enumerate(f):
        if k == 0:
            for i in range(int(line.split()[0])):
                nastepniki[i+1] = []
            continue
        l = tuple(map(int, line.split()))
        nastepniki[l[0]] += [l[1]]

    return nastepniki

def macierz_sasiedztwa(f):
    for k, line in enumerate(f):
        if k == 0:
            dlugosc = int(line.split()[0])
            macierz = [[0 for _ in range(dlugosc)] for _ in range(dlugosc)]
            continue
        l = tuple(map(int, line.split()))
        macierz[l[0]-1][l[1]-1] = 1
        macierz[l[1]-1][l[0]-1] = -1
    return macierz


if __name__ == "__main__":
    
    def print2d(m):
        for i in m:
            for j in i:
                print(j, end="\t")
            print()

    with open(input("Plik: "), "r") as f:
        plik = f.readlines()

    print(lista_nastepnikow(plik))
    print2d(macierz_sasiedztwa(plik))

