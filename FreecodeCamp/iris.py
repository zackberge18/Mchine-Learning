from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

iris=datasets.load_iris()

X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2)


