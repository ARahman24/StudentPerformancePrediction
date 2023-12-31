import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import sklearn.metrics

df = pd.read_csv("C:\\Users\\LATITUDE\\Desktop\\RBL\\dataaa.csv")
df['sex'] = df['sex'].map({'M': 0, 'F': 1})
df['address'] = df['address'].map({'U': 0, 'R': 1})
df['guardian'] = df['guardian'].map({'mother': 0, 'father': 1})
#df['internet'] = df['internet'].map({'no': 0, 'yes': 1})


predictors = df.values[:, 0:11]
targets = df.values[:,12]

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size= 0.25)


#print(pred_train.shape)
#print(pred_test.shape)
#print(tar_train.shape)
#print(tar_test.shape)

neigh = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')
neigh.fit(pred_train, tar_train)
y_pred = neigh.predict(pred_test)


#accuracy
print("Accuracy is ", accuracy_score(tar_test, y_pred, normalize = True))
a=accuracy_score(tar_test, y_pred, normalize = True)
a="{:.2f}".format(a)
#classification error
print("Classification error is",1- accuracy_score(tar_test, y_pred, normalize = True))
b=1- accuracy_score(tar_test, y_pred, normalize = True)
b="{:.2f}".format(b)
#sensitivity
print("sensitivity is", sklearn.metrics.recall_score(tar_test, y_pred, labels=None, average =  'micro', sample_weight=None))
c=sklearn.metrics.recall_score(tar_test, y_pred, labels=None, average =  'micro', sample_weight=None)
c="{:.2f}".format(c)
#specificity
print("specificity is", 1 - sklearn.metrics.recall_score(tar_test, y_pred,labels=None, average =  'micro', sample_weight=None))
d=1 - sklearn.metrics.recall_score(tar_test, y_pred,labels=None, average =  'micro', sample_weight=None)
d="{:.2f}".format(d)
a=float(a)*100
b=float(b)*100
c=float(c)*100
d=float(d)*100

x = np.array(["Accuracy", "ClassificationError", "Sensitivity", "Specificity"])
y = np.array([a,b,c,d])
plt.bar(x,y)
plt.show()
