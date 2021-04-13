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

