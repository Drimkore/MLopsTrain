import pandas as pd
import model_preparation

X_test = pd.read_csv("/test/x_test.csv", delimiter = ',')
y_test = pd.read_csv("/test/y_test.csv", delimiter = ',')

logreg.score(X_test, y_test)