tax = 0.27
cenabrutto1 = 100*(1+tax)
print(cenabrutto1)
cenabrutto2 = 450*(1+tax)
print(cenabrutto2)

name = "Fabian"
age = 38
height = 174.5
print('---\n')

# Mam na imie Fabian, mam 38 lat i 174.5 wzrostu
# 1 sposob f-string
print(f"Mam na imie {name}, mam {age} lat i {height} cm wzrostu")

# 2 sposob
print('Mam na imie', name, 'mam', age, 'lat', height, 'cm wzrostu')

# 3 sposob
full_text1 = 'Mam na imie ' + name +' mam ' + str(age) + ' lat i mam '+ str(height) + ' cm wzrostu '
print(full_text1)
print('---\n')

a1 = 2
h1 = 2
pole = (a1 * h1)/2
print(f"Trójkąt o podstawie {a1} i wysokości {h1} ma pole {pole}")

# TYPY DANYCH
name = 'Basia' #string
age = 38 #intriger - liczba calkowita
height = 174.5 #floating number - liczba zmiennoprzecinkowa
is_married = True #zmienna logiczna

data_type_desc = f'''Imie {name}i jest typu {type(name)} i jest wieku {age} jest {type(age)} zmienna wzrostu {height} 
to typ {type(height)} a zmienna {is_married} to typ {type(is_married)}'''
print(data_type_desc)

# import keyword ,sprawdzenie słow kluczowych
# print(keyword.kwlist)
