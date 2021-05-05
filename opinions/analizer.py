from os import listdir
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

print(*listdir("opinions"), sep="\n")

product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

opinions.pros = opinions.pros.replace([], None)

average_score = opinions.stars.mean()
opinions_count = opinions.shape[0]
pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()

print(f"""O produkcie dostępnych jest {opinions_count} opinii. 
Dla {pros_count} opinii podana została lista zalet, a dla {cons_count} lista wad.
Średnia ocena produktu wyznaczona na podstawie liczby gwiazdek wynosi {average_score:.1f}.""")

#pros_count = opinions.pros.notnull().count()

#rows_count = opinions.shape[0]

#print(rows_count, "=>", pros_count)


stars_count = opinions.stars.value_counts().reindex([True, False, float("Nan")], fill_value = 0)

ax = stars_count.plot.bar(color = "lightskyblue")

plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.title("Częstość występowania poszczególnych ocen produktu")
plt.savefig(f"./figures/{product_id}_stars.png")
plt.close()

recommendations = opinions.recommendation.value_counts(dropna = False).sort_index()
print(recommendations)
recommendations.plot.pie(
    label = "",
    labels = ['Polecam', 'Nie mam zdania', 'Nie polecam'],
    colors = ['forestgreen', 'crimson', 'orange'],
    autopct = "%1.1f%%",
    pctdistance = 1.2,
    labeldistance =1.4
)
plt.title("udział poszczególnych rekomendacji w ogólnej liczbie opinii")
plt.legend(bbox_to_anchor = (1.0,1.0))
plt.tight_layout()
plt.savefig(f"./figures/{product_id}_rcmd.png", bbox_inches = 'tight')
plt.close()

stars_recommendations = pd.crosstab(opinions.stars, opinions.recommendation.fillna('None'))
print(stars_recommendations)
