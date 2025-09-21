import numpy as np 

# array =  [[1,2,3,4],
#         [5,6,7,8], 
#         [9,10,11,12],
#         [13,14,15,16]] 

# array = np.array(array)

# #sum functions, takes axis argument to sum up all columns if axis = 0, and all rows if axis = 1 
# print(np.sum(array,axis =1))



# teens = array[array < 10]

# print(teens)

arrayRows = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
arrayColumns = np.array([[1,2,3,4,5,6,7,8,9,10]])


finalArray = arrayRows * arrayColumns

