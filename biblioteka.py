from datetime import datetime
import random
from datetime import datetime
from datetime import date
class Film:
    def __init__(self,tytul,rok_wydania,gatunek,liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
    def play_film(self, step = 1):
        self.liczba_odtworzen += step
    def __str__(self):
        return f'{self.tytul} ({self.rok_wydania})'
    
class Serial:
    def __init__(self,tytul,rok_wydania,gatunek,sezon,odcinek,liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.sezon = sezon
        self.odcinek = odcinek
        self.liczba_odtworzen = liczba_odtworzen
    def play_serie(self, step = 1):
        self.liczba_odtworzen += step
    def __str__(self):
        return f'{self.tytul} S{self.sezon:0>2}E{self.odcinek:0>2}'

lista = [Film(tytul="Independence Day", rok_wydania="1996", gatunek="SciFi", liczba_odtworzen = 500),
        Serial(tytul="Family guy", rok_wydania= "1999", gatunek="komedia", sezon="1", odcinek="1", liczba_odtworzen=900),
        Serial(tytul="Family guy", rok_wydania= "1999", gatunek="komedia", sezon="1", odcinek="2", liczba_odtworzen=1000),
        Film(tytul="Eternals", rok_wydania="2021", gatunek="akcja", liczba_odtworzen = 2000)]

def get_movies(lista):
    for film in lista:
        if isinstance(film, Film):
            x = f'{film.tytul} {film.rok_wydania} {film.gatunek} obejrzano {film.liczba_odtworzen} razy'
            print(x)

def get_series(lista):
    for serial in lista:
        if isinstance(serial, Serial):
            x = f'{serial.tytul} {serial.rok_wydania} {serial.gatunek} S{serial.sezon:0>2}E{serial.odcinek:0>2} obejrzano {serial.liczba_odtworzen} razy'
            print(x)

def search(lista,tytul):
    for element in lista:
        if element.tytul == tytul:
            print(element)

def top_titles():
    lista.sort(key = lambda x:x.liczba_odtworzen)
    print(lista)

def generate():
    for _ in range(10):
        generate_views(lista)

def generate_views(lista):
    choice = random.choice(lista)
    choice.liczba_odtworzen += random.randint(1,100)

#get_movies(lista)
#search(lista,"tytul")
#get_series(lista)

date = date.today()
print("Biblioteka filmów")
generate()
print(f"Najpopularniejsze filmy i seriale dnia {date.day}.{date.month}.{date.year}")
top_titles()
#nie wiem jak wyswietlic te najpopularniejsze filmy i zeby byly tylko 3 na koncu
#nie moge posortowac elementow z funkcji get_films i get_series alfabetycznie