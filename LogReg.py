from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split


df=pd.read_csv('adult.csv')

df['income']=df['income'].map({'<=50K':-1, '>50K':1})

X=df[['capital-gain','capital-loss','age','fnlwgt','educational-num','hours-per-week']]
y=df['income']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

