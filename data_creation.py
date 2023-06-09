import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('cars_moldova_clean.csv', delimiter = ',')




df['Target'] = np.where((df['Transmission']=='Automatic'), 1, 0)
df = df.drop(['Transmission'], axis=1)


num_columns = []
for column_name in df.columns:
    if (df[column_name].dtypes != object):
        num_columns +=[column_name]

X = df[num_columns].drop(['Target'], axis=1)
y = df['Target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


X_train.to_csv("train/x_train.csv", index=False)
pd.DataFrame(y_train).to_csv("train/y_train.csv", index=False)
X_test.to_csv("test/x_test.csv", index=False)
pd.DataFrame(y_test).to_csv("test/y_test.csv", index=False)
