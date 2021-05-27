# Praca domowa 7

## Zbiór danych

Poniższe zbiory zostały wyodrębnione ze zbioru [Wine UCI](https://archive.ics.uci.edu/ml/datasets/wine):


- train - bez próbek odstających, do trenowania modelu
- test - do oceny skuteczności modelu, dodana informacja o klasie 0=inliers, 1=outliers
- val - analogiczny do test, ale bez klasy

## Treść zadania

Celem zadania jest wykorzytanie algorytmu GMM do wykrywania próbek odstających.

Do oceny modelu wykorzystać metryki F1 score, Precision i Recall.
