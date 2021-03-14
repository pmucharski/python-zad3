#zad.1 Zdefiniuj następujące zbiory, wykorzystując Python comprehension:

# a= [1-x for x in range(10)]
# print(a)
#
# b= [4**y for y in range(7)]
# print(b)
#
# c= [x for x in a if x % 2 == 0]
# print(c)

#zad.2 Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj
# nową listę, która będzie zawierała tylko parzyste elementy

# liczby = [1,2,3,4,5,6,7,8,9,10]
# lista = [i for i in liczby if i % 2 == 0]
# print(lista)

#zad.3 Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość
# - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.

# sklep = {'chleb': 'sztuki', 'ryba': 'kg', 'masło': 'sztuki'}
# print(sklep)
# odwrocone = {value: key for key, value in sklep.items()}
# print(odwrocone)

#zad.4 Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
# def check(a, b, c):
#     if a == b == c:
#         return 'Trójkąt równoboczny'
#     if a >= b and a >= c:
#         if a ** 2 == b ** 2 + c ** 2:
#             return 'Trójkąt prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     elif b >= a and b >= c:
#         if b ** 2 == a ** 2 + c ** 2:
#             return 'Trójkąt prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     else:
#         if c ** 2 == b ** 2 + a ** 2:
#             return 'Trójkąt prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#
#
# print(check(3, 4, 5))
#
# #zad.5 Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
# def trapez(a=3, b=4, h=6):
#     return ((a + b) * h) / 2
#
#
# print(trapez())
#
# #zad.6 Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# # Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile elementów ma mnożyć)
# # Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
# def iloczyn(a=1, b=4, ile=10):
#     for elem in range(a, ile):
#         print(elem * b)
#
#
# iloczyn(3, 3, 13)
#
# #zad.7 Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.
# def fun(*liczby):
#     if len(liczby) != 3:
#         print('Podaj trzy liczby!')
#         return -1
#     for elem in range(liczby[0], liczby[2]):
#         print(elem * liczby[1])
#
#
# fun(1, 5, 4)
#
# #zad.8 Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.
# def licz(**kwargs):
#     return len(kwargs.items()), sum(x for x in kwargs.values())
#
#
# print(licz(mleko=15, zupa=3, kalafior=7))
#
# #zad.9 Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.
# from ciagi import *
#
# print(arytmetyczne.nwyraza(1, 10, 2))
# print(geometryczne.sumanwyrazow(1, 5, 5))

