import pandas as pd
import model_preparation
from model_preparation import logreg
import model_preprocessing as prep

X_test = pd.read_csv("test/x_test.csv", delimiter = ',')
y_test = pd.read_csv("test/y_test.csv", delimiter = ',')

print(logreg.score(prep.X_test, y_test))