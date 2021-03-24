# CeneoScraperS12

## Etap 1
### 1. analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)
|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion||
|ID opinii|['data-entry-id']|opinion_id||
|Autor|span.user-post__author-name|author||
|Rekomendacja|span.user-post__author-recomendation > em|recomencdation||
|Liczba gwiazdek|span.user-post__score-count|stars||
|Treść opinii|div.user-post__text|content||
|Lista zalet|div.review-feature__col:has|pros||
|Lista wad|cons||
|Czy potwierdzona zakupem|div.review-pz|purchased||
|Data wystawienia opinii|submit_date||
|Data zakupu produktu|span.|purchase_date||
|Dla ilu osób przydatna|useful||
|Dla ilu osób nieprzydatna|useless||


### 2. pobranie składowych pojedynczej opinii 
-pobranie kodu pojedycznej storny z opiniami 
-wyodrebnienie z kodu storny kodu pojedycznej opinii
-pobranie do pojedynczych zmiennych poszczególnych składowych na podstawie 