from kahn_ln import test_kahn_ln
from tarjan_ms import test_tarjan_ms
from tarjan_ln import test_tarjan_ln
from kahn_ms import test_kahn_ms

if __name__ == "__main__":
    import os
    def clear(wait = True):
        if wait:
            input()
        os.system('cls' if os.name == 'nt' else 'clear')

    clear(0)
    print("==================================")
    print("  TOPOLOGICZNE SORTOWANIE GRAFÓW ")
    print("==================================")
    
    filename = input("Podaj nazwę pliku z reprezentacją grafu: ")
    try:
        with open(filename, "r") as f:
            plik = f.readlines()
    except FileNotFoundError:
        print(f"Plik {filename} nie został znaleziony.")
        exit(1)
    
    clear(0)
    while True:
        print("WYBIERZ ALGORYTM:")
        print("1 - Algorytm Kahna - lista następników")
        print("2 - Algorytm Kahna - macierz sąsiedztwa")
        print("3 - Algorytm Tarjana - lista następników")
        print("4 - Algorytm Tarjana - macierz sąsiedztwa")
        print("0 - Wyjście")
        
        menu = input("Twój wybór: ")
        match menu:
            case "1":
                test_kahn_ln(plik)
                clear()
            case "2":
                test_kahn_ms(plik)
                clear()
            case "3":
                test_tarjan_ln(plik)
                clear()
            case "4":
                test_tarjan_ms(plik)
                clear()
            case "0":
                break
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

