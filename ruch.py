class Ruch:
    def __init__(self, user_input, obecny_x, obecny_y, obecny_kierunek, rozmiar):
        self.user_input = user_input
        self.obecny_x = obecny_x
        self.obecny_y = obecny_y
        self.obecny_kierunek = obecny_kierunek
        self.rozmiar = rozmiar
        self.obecny_stopien = self.konwersja_kierunek_na_stopien()
        self.wlasciwosci = {"360": "N", "90": "E", "180": "S", "270": "W"}
        # self.wlasciwosci = {"360": {"kierunek": "N"}, "90": {"kierunek": "E"},
        #                           "180": {"kierunek": "S"}, "270": {"kierunek": "W"}}

    def konwersja_kierunek_na_stopien(self):
        if self.obecny_kierunek == "N":
            return 360
        elif self.obecny_kierunek == "E":
            return 90
        elif self.obecny_kierunek == "S":
            return 180
        elif self.obecny_kierunek == "W":
            return 270


    def convert_input(self):
        for litera in self.user_input:
            if litera == "M":
                if self.obecny_kierunek == "N":
                    self.obecny_y += 1
                    if self.obecny_y >= self.rozmiar:
                      self.obecny_y = self.rozmiar-1
                elif self.obecny_kierunek == "E":
                    self.obecny_x += 1
                    if self.obecny_x >= self.rozmiar:
                      self.obecny_x = self.rozmiar-1
                elif self.obecny_kierunek == "S":
                    self.obecny_y -= 1
                    if self.obecny_y < 0:
                      self.obecny_y = 0
                elif self.obecny_kierunek == "W":
                    self.obecny_x -= 1
                    if self.obecny_x < 0:
                      self.obecny_x = 0
            elif litera == "R":
                self.obecny_stopien += 90
                if self.obecny_stopien == 450:
                    self.obecny_stopien = 90
                self.obecny_kierunek = self.wlasciwosci.get(str(self.obecny_stopien))
            elif litera == "L":
                self.obecny_stopien -= 90
                if self.obecny_stopien == 0:
                    self.obecny_stopien = 360
                self.obecny_kierunek = self.wlasciwosci.get(str(self.obecny_stopien))
        return self.obecny_x, self.obecny_y, self.obecny_kierunek