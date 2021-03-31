# Zadanie domowe 3
W realizacji zadania skorzystaj ze zbioru danych pogodowych w Australii (*australia.csv*).

### Opis danych
Zbiór danych zawiera codzienne obserwacje pogody z wielu australijskich stacji pogodowych. Waszym zadaniem będzie stworzenie modelu klasyfikacyjnego, który będzie potrafił przewidzieć czy następnego dnia będzie padał deszcz czy też nie.

##### Kolumny:
- **MinTemp** - Minimalna temperatura [C]
- **MaxTemp** - Maksymalna temperatura [C]
- **Rainfall** - Suma opadów [mm]
- **Evaporation** - Miara odparowywania [mm]
- **Sunshine** - Suma czasu nasłonecznienia [h]
- **WindGustSpeed** - Najwyższa prędkość wiatru [km/h]
- **WindSpeed9am** - Prędkość wiatru o 9:00 [km/h]
- **WindSpeed3pm** - Prędkość wiatru o 15:00 [km/h]
- **Humidity9am** - Wilgotność o 9:00 [%]
- **Humidity3pm** - Wilgotność o 15:00 [%]
- **Pressure9am** - Ciśnienie atmosferyczne o 9:00 [hPa]
- **Pressure3pm** - Ciśnienie atmosferyczne o 15:00 [hPa]
- **Cloud9am** - Zachmurzenie o 9:00 [skala: 0 - słońce, 8 - całkowite zachmurzenie]
- **Cloud3pm** - Zachmurzenie o 15:00 [skala: 0 - słońce, 8 - całkowite zachmurzenie]
- **Temp9am** - Temperatura o 9:00 [C]
- **Temp3pm** - Temperatura o 15:00 [C]
- **RainToday** - Czy dzisiaj padał deszcz [0 - nie, 1 - tak]
-  **Zmienna celu:** **RainTomorrow** - Czy jutro będzie padał deszcz [0 - nie, 1 - tak]

Dane pochodzą z https://www.kaggle.com/jsphyg/weather-dataset-rattle-package. Natomiast nasz zbiór jest już przygotowany do pracy i nie zawiera brakujących wartości i kolumn z tekstem.

### Treść zadania
Podstawowa część zadania polega na wytrenowaniu dowolnych 3 klasyfikatorów i sprawdzeniu ich skuteczności.
Raport powinien zawierać:
- podział danych na zbiór treningowy i testowy
- nauczenie 3 dowolnych klasyfikatorów
- w każdym klasyfikatorze należy wybrać minimum jeden hiperparametr (nie trzeba go stroić - wystarczy się zapoznać z parametrami modelu)
- wykorzystanie przynajmniej 3 miar oceny jakości klasyfikatorów i wybór najlepszego z nich.


Rozwiązania (Jupyter Notebook + html) proszę zgłaszać przez pull request do podfolderu z imieniem i nazwiskiem.

Termin oddania: 9/13 IV 2020 r. w momencie rozpoczęcia zajęć
