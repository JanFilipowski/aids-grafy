
from collections import deque

def kahn_ln(nastepniki):
    in_degree = {v: 0 for v in nastepniki}

    for u in nastepniki:
        for v in nastepniki[u]:
            in_degree[v] += 1

    queue = deque([v for v in nastepniki if in_degree[v] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in nastepniki[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result if len(result) == len(nastepniki) else None


def test_kahn_ln(f):
    from representation import lista_nastepnikow
    lista = lista_nastepnikow(f)
    wynik = kahn_ln(lista)
    print(wynik if wynik is not None else "Graf zawiera cykl")


# TESTOWANIE FUNKCJI
if __name__ == "__main__":
    with open(input("Plik: "), "r") as f:
        plik = f.readlines()
    test_kahn_ln(lista)