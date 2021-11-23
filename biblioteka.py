class film:
    def __init__(self,film_tytul,film_rok_wydania,film_gatunek,film_liczba_odtworzen):
        self.film_tytul = film_tytul
        self.film_rok_wydania = film_rok_wydania
        self.film_gatunek = film_gatunek
        self.film_liczba_odtworzen = film_liczba_odtworzen
        def play_film(self, odtw = 1)
            self.liczba_odtworzen += odtw
    def __str__(self):
        return f'{self.film_tytul} ({self.film_rok_wydania})'
    
class serial:
    def __init__(self,serial_tytul,serial_rok_wydania,serial_gatunek,serial_sezon,serial_odcinek,serial_liczba_odtworzen):
        self.serial_tytul = serial_tytul
        self.serial_rok_wydania = serial_rok_wydania
        self.serial_gatunek = serial_gatunek
        self.serial_sezon = serial_sezon
        self.serial_odcinek = serial_odcinek
        self.serial_liczba_odtworzen = serial_liczba_odtworzen
        def play_serie(self, odtw = 1)
            self.serial_liczba_odtworzen += odtw
    def __str__(self):
        return f'{self.serial_tytul} S{self.serial_sezon:02}E{self.serial_odcinek:02}'

films = film(film_tytul="Dzień niepodległosci", film_rok_wydania="1996", film_gatunek="SciFi", film_liczba_odtworzen = 500)
series1 = serial(serial_tytul="Family guy", serial_rok_wydania= "1999", serial_gatunek="komedia", serial_sezon="1", serial_odcinek="1", serial_liczba_odtworzen=900)
series2 = serial(serial_tytul="Family guy", serial_rok_wydania= "1999", serial_gatunek="komedia", serial_sezon="1", serial_odcinek="2", serial_liczba_odtworzen=1000)
lista = [films,series1,series2]
