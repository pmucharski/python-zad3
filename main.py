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
