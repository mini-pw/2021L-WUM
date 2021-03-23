# Zadanie domowe 2

W realizacji zadania skorzystaj ze zbioru Allegro [https://www.dropbox.com/s/360xhh2d9lnaek3/allegro-api-transactions.csv?dl=1] 
Zadanie składa się z dwóch części:
1. Kodowanie zmiennych kategorycznych 

Wykonaj target encoding dla zmiennej it_location (+ komentarz jaka jest przewaga tej metody nad one-hot encoding). Jako target traktujemy kolumnę price (będzie to więc zadanie regresji). 
Zastosuj trzy metody encodingu (one-hot + "dwie nowe") dla kolumny main_category. "Nowe metody" proszę wybrać spośród wymienionych na stronie https://contrib.scikit-learn.org/category_encoders/. W przypadku gdy użyta metoda nie działa proszę o stosowną adnotację. Opisz wyniki.


2. Uzupełnianie braków

W tej części zadania traktujemy zmienną price nie jak target a zmienną objaśniającą. Zbiór danych ograniczamy do zmiennych numerycznych tj. price, it_seller_rating i it_quantity. 
Proszę losowo usunąć 10% wartości ze zmiennej it_seller_rating i je uzupełnić z użyciem 2 narzędzi: Nearest neighbors imputation i Multivariate feature imputation (https://scikit-learn.org/stable/modules/impute.html). Następnie należy porównać wartości imputowane z oryginalnymi (polecam miarę RMSE). Eksperyment powtórzyć 10 razy i zobaczyć jakie będzie odchylenie standardowe wyników. Następnie zrobić analogiczną analizę gdy oprócz losowego usuwania 10% wartości z kolumny it_seller_rating usuniemy także losowo 10% ze zmiennej it_quantity. (w przypadku problemów wydajnościowych proszę ograniczyć liczbę rekordów). Opisać wnioski z analizy i umieścić podsumowujący wykres.


Rozwiązania (Jupyter Notebook + pdf) proszę zgłaszać przez pull request do podfolderu z imieniem i nazwiskiem.
