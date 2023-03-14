from sklearn.linear_model import LogisticRegression
import model_preprocessing as prep
import y_train

logreg = LogisticRegression()
logreg.fit(prep.X_train, y_train)
logreg.score(prep.X_train, y_train)




