import os
import sys
import numpy as np
import pandas as pd

f = open("F:/Descargas/ERIC2025-04-22_07.43.26.nbib")

read = f.readlines()
lines = []

for line in read:
    lines.append(line)

entries = []
authors = []
title = []
types = []
journals = []

total = []
total_columns = ("entry", "authors", "title", "type", "journal")

count = 0

for i in lines:
    aut = []
    if i == ";\n":
        count = count + 1
        entries.append(count)
        total.append(list((entries, authors, title, types, journals)))

        
        entries = []
        authors = []
        title = []
        types = []
        journals = []

    try:
        a, b = i.split(" - ")
        if a == "AU ":
            authors.append(b.replace("\n",""))
            print(authors)
        elif a == "JT ":
            journals.append(b.replace("\n",""))
        elif a == "TI ":
            title.append(b.replace("\n",""))
        elif a == "PT ":
            types.append(b.replace("\n",""))
    except:
        pass
    
print(total)

df = pd.DataFrame(total)
df.to_csv("F:/Descargas/converted.csv", index=False)

