class film:
    def __init__(self,tytul,rok_wydania,gatunek,liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
        self.liczba_odtworzen = 0
        def play(self, odtw = 1)
            self.liczba_odtworzen += odtw
    def __str__(self):
        return f'{self.tytul} ({self.rok_wydania})'
class serial:
    def __init__(self,tytul,rok_wydania,gatunek,sezon,odcinek,liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.sezon = sezon
        self.odcinek = odcinek
        self.liczba_odtworzen = liczba_odtworzen
        self.liczba_odtworzen = 0
        def play(self, odtw = 1)
            self.liczba_odtworzen += odtw
    def __str__(self):
    return f'{self.tytul} S{self.sezon:02}E{self.odcinek:02}'
