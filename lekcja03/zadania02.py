# -> zadanie 1
#     Stwórz listę wszystkich liczb dwucyfrowych podzielnych przez 5.
#     Sprawdź, czy lista ma parzystą czy nieparzystą długość.
#     Jeśli długość jest parzysta, usuń pierwszy element.
#     Wyznacz środkowy element listy i go wyświetl.

# lista = list(range(10,100,5))
# print(lista)
# print('---\n')
# lista = lista[1:]
# print(lista)
# print(len(lista))
# print(lista[len(lista)//2])

# -> zadanie 2
#     Stwórz listę wszystkich liter alfabetu angielskiego (od 'a' do 'z').
#     Wyświetl literę znajdującą się w środku listy.
#     Odwróć listę i wyświetl pierwsze 5 elementów z odwróconej listy.
#     Wyświetl co drugą literę z listy.

# lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z']
# print(len(lista))
# mylist = lista[::-1][:5]
# print(mylist)

# rozgrzewka
# wygeneruj listę liczb od 1 do 150
# wyświetl tylko te elementy i parzystych indexach

# lista = list(range(1,151,))
# print(lista[2::2])

# -> zadanie 3
#     Wygeneruj listę wszystkich liczb podzielnych przez 7 w zakresie od 100 do 1000.
#     Wyświetl element o indeksie 50.
#     Wyświetl przedostatni element listy.
#     Wyświetl co 5-ty element listy.

# mylist = list(range(105,1001, 7))
# print(mylist)
# print(mylist [50])
# print(mylist [-2])
# print(mylist [:5])

# -> zadanie 4
    # Utwórz listę wszystkich liczb od 100 do 0 włącznie, w kolejności malejącej.
    # Wyświetl pierwsze 10 elementów tej listy.
    # Wyświetl ostatnie 10 elementów tej listy.
    # Wyświetl co 7-my element listy.
    # Odwróć listę ponownie (tak, aby była rosnąca) za pomocą slicing.

# mylsit = list(range(0,101))
# lista = (mylsit [::-1])
# # print(lista [:10])
# # print(lista [-10:])
# # print(lista [::7])
# lista = (mylsit [1::])
# print(lista)

# -> zadanie 5
    # wygeneruj liste wszystkich liczb 3-cyforwych parzystych
    # wyświetl srodkowy element takiej listy
    # jesli taka lista nie ma srodkowego elementu - wyświetl średnia artymetyczna dwóch środkowych elementówccc

# lista = list(range(100,999,2))
# print(lista)
# print([len(lista) // 2])

# Utwórz zbiór unique_numbers z listy zawierającej powtarzające się liczby
# Dodaj do niego nowy element, a następnie usuń dowolny element

#

# Utwórz pusty zbiór my_set, dodaj do niego kilka elementów, a następnie:
    # usuń jeden z nich przy pomocy discard()
    # spróbuj usunąć nieistniejący element przy pomocy remove() (sprawdź co się stanie)
    # wyczyść zbiór

# empty_set = set()
# print(empty_set)
# empty_set.add(1)
# empty_set.add(2)
# empty_set.add(3)
# empty_set.add(4)
# print(empty_set)
# empty_set.discard (1)
# print(empty_set)
# # empty_set.remove (300)
# # print(empty_set)
# empty_set.clear()
# print(empty_set)

# Utwórz zbiór zawierający:
    # liczbę całkowitą,
    # liczbę zmiennoprzecinkową,
    # napis,
    # krotkę,
    # wartość logiczną.
# Spróbuj dodać do niego listę i słownik, obserwując co się stanie.

# tupla = tuple([1,2,3,4,5])
# my_set = {2,4.5,"Aga",False,tupla}
# print(my_set)

# dana jest tupla:
letters = ('a', 'b', 'a', 'c', 'a', 'd', 'b')
# Policz, ile razy występuje litera 'a'
# Znajdź indeks pierwszego wystąpienia litery 'b'
# Spróbuj znaleźć indeks litery 'z' (co się stanie?)
