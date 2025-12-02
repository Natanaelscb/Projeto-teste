import pandas as pd
lista=[12,21,54,21,15.8]
s = pd.Series(lista)

dict = {
    "Nomes":["matheus","fabio","natan"],
    "Notas":[2,4,8],
    "Idades":[16,30,45]
}
df = pd.DataFrame(dict)
#print(df)
#print(df.columns.to_list())
#print(df.loc[2])
df["aprovado"] = df["Notas"]>=7
print(df)