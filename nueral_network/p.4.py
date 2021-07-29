import numpy as np

inputs=[[1,2,3,4],
        [3,4,5,6],
        [5,6,7,8]]
weights=[[5,6,7,8],
         [1,2,3,4],
         [5,4,3,6]]
bias=[1,2,4]
output=np.dot( inputs,np.array(weights).T)+bias
print(output)