import os
import sys
import numpy as np
import pandas as pd

file = str(input("Please, enter the NBIB file to convert to CSV: "))
f = open(file)

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
out_file = file.replace(".nbib", ".csv")
df.to_csv(out_file, index=False)

