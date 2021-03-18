# Zadanie domowe 2

W realizacji zadania skorzystaj ze zbioru Allegro [https://www.dropbox.com/s/360xhh2d9lnaek3/allegro-api-transactions.csv?dl=1]  
Zadanie składa się z dwóch części:
1. kodowanie zmiennych kategorycznych

Wykonaj target encoding dla zmiennej it_location. Czy i jakie są przewagi target encoding nad one-hot? Jako target traktujemy kolumnę price (będzie to więc zadanie regresji).  
Zastosuj trzy metody encodingu (one-hot + "dwie nowe") dla kolumny main_category. "Nowe metody" proszę wybrać spośród wymienionych na stronie https://contrib.scikit-learn.org/category_encoders/. W przypadku, gdy użyta metoda nie działa proszę o stosowną adnotację. Opisz wyniki.

 Zwizalizuj wynik oraz wyjaśnij czym się różnią sposoby kodowania (czemu to działa).

2. uzupełnianie braków

W tej części zadania traktujemy zmienną price nie jak target a zmienną objaśniającą. Zbiór danych ograniczamy do zmiennych numerycznych tj. price, it_seller_rating i it_quantity.  
Proszę losowo usunąć 10% wartości ze zmiennej it_seller_rating i je uzupełnić z użyciem jednego z automatycznych narzędzi: Nearest neighbors imputation lub Multivariate feature imputation (https://scikit-learn.org/stable/modules/impute.html).  
Następnie należy porównać wartości imputowane z oryginalnymi (polecam miarę RMSE). Eksperyment powtórzyć 10 razy i zobaczyć jakie będzie odchylenie standardowe wyniku. Następnie zrobić analogiczną analizę gdy oprócz losowego usuwania 10% wartości z kolumny it_seller_rating usuniemy także losowo 10% ze zmiennej it_quantity. (w przypadku problemów wydajnościowych proszę ograniczyć liczbę rekordów).  
Opisać wnioski z analizy jakości imputacji i umieścić podsumowujący wykres.


Rozwiązania (Jupyter Notebook + html) proszę zgłaszać przez pull request do podfolderu z imieniem i nazwiskiem.

Termin oddania: 23/26 III 2021 r. w momencie rozpoczęcia zajęć.
