from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import svm
iris=datasets.load_iris()

X=iris.data
y=iris.target

classes=['Iris Setosa',"Iris Versicolour","Iris Virginica"]
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2)

model=svm.SVC()

model.fit(X_train, y_train)

prediction=model.predict(X_test)

acc=accuracy_score(y_test,prediction)
print("real :",y_test)
print("fake :",prediction)
for i in range(len(prediction)):
    classes[prediction[i]]
print(acc)


