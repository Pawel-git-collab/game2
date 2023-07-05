from plansza import Plansza
from ruch import Ruch

x = 0
y = 0
kierunek = "N"
rozmiar = 5
_plansza = Plansza(x, y, rozmiar=rozmiar)


while True:
    _plansza.drukuj_plansze()
    user_input = input("Podaj dane do ruchu M, R, L: ")
    obecny_x = _plansza.kierunek_X
    obecny_y = _plansza.kierunek_Y
    _ruch = Ruch(user_input, obecny_x, obecny_y, kierunek, rozmiar)
    nowy_x, nowy_y, kierunek = _ruch.convert_input()
    print(f"Obecna pozycja: {nowy_x} {nowy_y} {kierunek}")
    _plansza.ustaw_klocek(nowy_x, nowy_y)







