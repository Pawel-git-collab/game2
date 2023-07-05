class Plansza:
    def __init__(self, kierunek_X=0, kierunek_Y=0, rozmiar=5):
        self.rozmiar = rozmiar
        self.kierunek_X = kierunek_X
        self.kierunek_Y = kierunek_Y
        self.znak_klocka = "x"
        self.znak_planszy = "-"
        self.plansza = self.generuj_plansze()

    def generuj_plansze(self):

        plansza = [["-" for x in range(self.rozmiar)] for y in range(self.rozmiar)]
        plansza[self.kierunek_X][self.kierunek_Y] = self.znak_klocka
        return plansza

    def drukuj_plansze(self):
        for i, rzad in enumerate(reversed(self.plansza)):
            print("{} {}".format(self.rozmiar-i-1, " ".join(rzad)))
        cyfry_col = [i for i in range(self.rozmiar)]
        print(" ", *cyfry_col)

    def ustaw_klocek(self, x, y):


        self.plansza[y][x] = self.znak_klocka
        if self.kierunek_X != x or self.kierunek_Y != y:
            self.plansza[self.kierunek_Y][self.kierunek_X] = self.znak_planszy
        # ten kod usuwa nam klocek w jednym miejscu i przekazuje do drugiego miejsca
        self.kierunek_X, self.kierunek_Y = x, y