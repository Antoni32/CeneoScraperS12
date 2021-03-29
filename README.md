# CeneoScraperS12
## Etap 1
### 1. analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|obiekt bs4>elemnt.Tag|
|ID opinii|['data-entry-id']|opinion_id|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recommendation > em|recomencdation|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista zalet|div.review-feature__col:has|pros|list|
|Lista wad|cons|list|
|Czy potwierdzona zakupem|div.review-pz|purchased|bool|
|Data wystawienia opinii|submit_date|str|
|Data zakupu produktu|span.|purchase_date|str|
|Dla ilu osób przydatna|useful|int|
|Dla ilu osób nieprzydatna|useless|int|


### 2. pobranie składowych pojedynczej opinii 
-pobranie kodu pojedycznej storny z opiniami 
-wyodrebnienie z kodu storny kodu pojedycznej opinii
-pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie 
-obsługa błędów