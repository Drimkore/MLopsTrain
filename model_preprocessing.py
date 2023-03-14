from sklearn import preprocessing
from data_creation import X_train, X_test

scaler = preprocessing.MinMaxScaler()
X_train = scaler.fit_transform(X_train.values)
X_test = scaler.fit_transform(X_test.values)



