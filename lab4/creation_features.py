import pandas as pd
import numpy as np

df = pd.read_csv('/home/art/gitproj/MLopsTrain/data/cars_moldova_clean.csv', delimiter = ',')
df_1 = df[['Make', 'Model', 'Year', 'Style', 'Price(euro)', 'km_year']]
df_1.to_csv('/home/art/gitproj/MLopsTrain/data/cars_moldova_clean.csv', index=False)


#df = pd.read_csv('/home/art/gitproj/MLopsTrain/data/cars_moldova_clean.csv', delimiter = ',')
#counts = df.Make.value_counts() 
#counts.median()
#rare =  counts[(counts.values < 25)]
#df['Make'] = df['Make'].replace(rare.index.values, 'Rare')
#df.to_csv('/home/art/gitproj/MLopsTrain/data/cars_moldova_clean.csv', index=False)



#df = pd.read_csv('/home/art/gitproj/MLopsTrain/data/cars_moldova_clean.csv', delimiter = ',')
#hotEncoded = pd.get_dummies(df)
#hotEncoded.to_csv('/home/art/gitproj/MLopsTrain/data/cars_moldova_clean.csv', index=False)
