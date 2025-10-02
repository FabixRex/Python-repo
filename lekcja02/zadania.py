#Zadanie 9 dotyczy przedziałów liczbowych
wiek = int(input('podaj swoj wiek: '))
if wiek < 10:
    print('Kategoria: dzieci')
elif 10 <= wiek >= 17:
    print('Kategoria: mlodziez')
elif 18 <= wiek >= 40:
    print('Kategoria: dorosli')
else:
    print('Kategoria: seniorzy')