from sklearn.linear_model import LogisticRegression
import model_preprocessing as prep
from data_creation import y_train

logreg = LogisticRegression()
logreg.fit(prep.X_train, y_train)
print(logreg.score(prep.X_train, y_train))




