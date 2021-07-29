from sklearn import datasets

from sklearn import linear_model

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

boston=datasets.load_boston()
#features/label

X=boston.data
y=boston.target

print(X.shape)
print(y.shape)

l_reg=linear_model.LinearRegression()


plt.scatter(X.T[5],y)

plt.show()


X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2)

#train
model=l_reg.fit(X_train,y_train)

prediction=model.predict(X_test)
# acc=accuracy_score(y_test,prediction)
print("fake: ",prediction)
print("Real : ",y_test)
# print(acc)
print("r^2:",l_reg.score(X,y))
print("coeed:",l_reg.coef_)
print("intercep:",l_reg.incercept)
plt.scatter(prediction,y_test)

plt.show()
