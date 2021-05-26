# Praca domowa 6

## Dataset

Analizowany zbiór danych: Olivetti Faces

Jak wczytać:

```python
from sklearn.datasets import fetch_olivetti_faces
```

## Treść zadania

0. Narysować wybrane obrazy.
1. Wykorzystać algorytm PCA do kompresji zbioru Olivetti Faces. Dobrać odpowiednią liczbę składowych. Po transformacji obliczyć [stopień kompresji](https://pl.wikipedia.org/wiki/Stopie%C5%84_kompresji). Rozmiar obrazka: liczba wartości numerycznych
2. Przeprowadzić transformację odwrotną (inverse_transform). Narysować, porównać z pkt. 0. Obliczyć błąd rekonstrukcji w postaci błędu RMSE dla każdego obrazu.
3. Przygotować kilka / kilkanaście zmodyfikowanych obrazów (np. obróconych o 90 stopni, przyciemnionych, odbitych w poziomie).
4. Korzystając z modelu wyuczonego w pkt. 1 przeprowadzić transformację, a następnie odwrotną transformację obrazów z pkt. 3. Obliczyć błąd rekonstrukji dla każdego typu modyfikacji. Porównać z wartościami błędu uzyskanymi w pkt. 2.
5. Czy PCA może służyć do wykrywania pewnego typu anomalii w zdjęciach twarzy? Jeżeli tak to jakich?
