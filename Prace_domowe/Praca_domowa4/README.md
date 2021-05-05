# Zadanie domowe 4

Zadanie dotyczy algorytmu Support Vector Machine, który był omówiony na zajęciach. Zainteresowanych zachęcamy do zapoznania się z http://pyml.sourceforge.net/doc/howto.pdf.

Wykorzystaj dwa zbiory danych:

  - apartments z R-owego pakietu DALEX,
  - dowolny, wybrany przez siebie zbiór danych (najlepiej z co najmniej 8 zmiennymi numerycznymi).

1. Dopasuj SVM do obu zbiorów danych.
2. Sprawdź, czy zalinkowany artykuł słusznie zwraca uwagę na skalowanie danych (pamiętaj, że większość implementacji domyślnie skaluje).
3. Spróbuj zoptymalizować metodą random search najważniejsze hiperparametry tj. :
* cost,
* gamma,
* degree, 
najprościej optymalizować hiperparametry w SVM z jądrem gaussowskim, ale można też poszukać najlepszego jądra.


## Zadanie bonusowe za 2 punkty (uwzględnione w całościowej punktacji przedmiotu) 

Aby uzyskać bonusowy punkt należy wykorzystać po raz kolejny zbiór danych z PD2 i nauczyć dowolny modele regresji do prognozowania zmiennej price (traktujemy ją teraz jak zmienną celu). W kwestii zmiennych objaśniających należy się ograniczyć do main_category, categories i it_location.  

Rozwiązanie powinno zawierać: 
- zastosowanie target encodingu (należy przemyśleć parametr smoothing i wyjaśnić dlaczego jest on ważny)
- nauczenie modelu liniowego do przewidywania ceny produktu  
- zastosowanie co najmniej dwóch wariantów regularyzacji i przeanalizowanie ich wpływu na jakość predykcji (należy dodać krótki opis zastosowanych metod) 
- nauczenie innego modelu regresyjnego  
- wykorzystanie miary RMSE i R2 do wybrania najlepszego wariantu modelu 
