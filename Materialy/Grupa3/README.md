## Prace domowe
Wrzucamy:
* notebooki wyczyszczone z outputu 
* pdf z outputem
### Zajęcia 1 
Tutaj przykład z EDA z kaggla o którym mówiłem, przejrzyjcie sobie i użyjcie jakiejś techniki w pracy domowej.
https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python

### Zajęcia 2

#### Missing values imputation methods

Wszystkie metody o których mówiliśmy, mają swoją implementację w scikicie (dzięki czemu można ich łatwo używać w pipelinach)
* [Mean / median / most frequent imputation](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer)
* [Missing values indicator](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator)

Metoda o której wspomniałem (tylko nie opiera się na zmiennej celu tylko na wszystkich zmiennych):
 https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer

#### Encoding 
* [Datatime cyclical encoding](https://www.avanwyk.com/encoding-cyclical-features-for-deep-learning/)
* [Multi label encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html)
