import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import datasets ## imports datasets from scikit-learn
data = datasets.load_boston() ## loads Boston dataset from datasets library
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn import svm
# define the data/predictors as the pre-set feature names  
df = pd.DataFrame(data.data, columns=data.feature_names)

# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=['MEDV'])

X = df[['CRIM','ZN']]
y = target['MEDV']
lm = linear_model.LinearRegression()
model = lm.fit(X,y)
predictions = lm.predict(X)
#print(predictions[0:5])

print("Whole data R^2=",r2_score(target['MEDV'],predictions))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
model = lm.fit(X_train,y_train)
predictions = lm.predict(X)
print("Split 80-20 rows R^2=",r2_score(target['MEDV'],predictions))

#clf = svm.SVC()
#scores = cross_val_score(clf, data.data, data.target, cv=2)
#print(scores)

#print(predictions[0:5])
#print("Accuracy:",metrics.accuracy_score(y_test,predictions))
'''X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
model = lm.fit(X_train,y_train)
predictions = lm.predict(X)
print("20 rows R^2=",r2_score(target['MEDV'],predictions))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)
model = lm.fit(X_train,y_train)
predictions = lm.predict(X)
print("30 rows R^2=",r2_score(target['MEDV'],predictions))

'''


'''
# Check if split is actually correct
# We can see it's roughly 80% train and 20% train
# So we can proceed!
print(float(X_train.shape[0]) / float(y.shape[0]))
print(float(X_test.shape[0]) / float(y.shape[0]))'''