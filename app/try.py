import pandas as pd

df = pd.read_csv("/Users/abhishek//Downloads/text.csv")
df1 = df['Quantity Shipped'].apply(pd.to_numeric, errors='coerce')


print df1