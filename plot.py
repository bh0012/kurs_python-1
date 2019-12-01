import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df["E"] =df["A"] + df["B"] #tworzymy kolumnę E, która będzie sumą wartości kolumn A i B
a = df["E"].sum() #daje nam sumę wszystkich wartości w kolumnie
#df.to_csv("tablica.csv") # to daje nam możliwość zapisania do pliku CSV


df1 = pd.read_csv("tablica.csv") # jeśli program jest w tym samym folderze co plik, to podaję tylko nazwę pliku, ale jeśli są w innych, to trzeba podać całą ścieżkę
print(df[["A", "B", "E"]])
print(a)
