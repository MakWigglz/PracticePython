import pandas as pd

# read excel as pd
df = pd.read_excel("rtirevisiontrianglenov.xlsx", engine="openpyxl")
pyscript.write("output", df.head().to_html())
df1 = pd.read_csv("median_pay.csv")
pyscript.write("output-2", df1.head().to_html())
df2 = pd.read_csv("mp-comments-table.csv")
pyscript.write("output-3", df2.head().to_html())
print(df.head())
print(df1.head())
print(df2.head())
