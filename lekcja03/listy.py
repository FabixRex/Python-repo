# my_list = [12, 'jakis napis', 12.34, True, None, [1,2,3]]
#
# print(type(my_list[-1]))
# print(type(my_list[0]))


# my_list = [12, 'jakis napis', 12.34, True, None, [1,2,3]]
#
# print(type(my_list[0]))
#
# print(type(my_list[1]))
# print(type(my_list[2]))
# print(type(my_list[3]))
# print(type(my_list[-2]))
# print(type(my_list[-1]))
#
# print('------\n')
#
# inner_list = my_list[-1]
# print(inner_list)
# print(inner_list[-1])
# print('------\n')

# wygeneruj listę wszystkich liczb parzystych trzycyfrowych
# i znajdz jej srodkowy element

print(list(range(100,1000,2)))
lista = list(range(100,1000,2))
print(len(lista))
if len(lista) % 2 == 0:
    print('bark elementu środkowego')
else:
    print(lista[len(lista)//2])

    print('------\n')

    len(lista)
    if len(lista) % 2 == 0:
        lista = lista[:-1]
    print(lista[len(lista) // 2])