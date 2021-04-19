# CeneoScraperS12
## Etap 1 Ekstrakcja pojedynczej opinii, którego kod będzie wpisany w kodzie programu
### 1. analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|obiekt bs4>elemnt.Tag|
|ID opinii|['data-entry-id']|opinion_id|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation > em|recommencdation|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista zalet|div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item|pros|list|
|Lista wad|div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item|cons|list|
|Czy potwierdzona zakupem|div.review-pz|purchased|bool|
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|submit_date|str|
|Data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|int|


### 2. pobranie składowych pojedynczej opinii
- pobranie kodu pojedycznej storny z opiniami 
- wyodrebnienie z kodu storny kodu pojedycznej opinii
- pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie 
- obsługa błędów
- dobranie typów danych do wartości zmiennych

## Etap 2 Ekstracja wszystkich opinii o produkcie z pojedynczej strony
- zapis składowych pojedynczej opinii do słownika
- zdefiniowanie listy do przechowywania wszystkich opinii o danym produkcie
- dodanie pętli, która wykonuje operacje ekstrakcji dla wszystkich opinii pobranych z pojedynczej strony

## Etap 3 Ekstracja wszystkich opinii o produkcie z wszystkich stron
- dodanie pętli, która pobiera i analizuje kolejne strony z opiniami o produkcie 
- dodanie możliwości podania kodu produktu "z klawiatury" 
- dodanie zapisu wszystkich opinii o produkcie do pliku .json
- 