
"""
Fungsi untuk memeriksa apakah ada duplikasi data di list.

eee.sunupradana.info
2022

"""

import numpy as np


test_data1 = [ 0, 93, 76, 88, 25, 83, 30, 66, 27, 64, 59, 25, 71, 36, 65, 40, 39, 72, 43, 88, 83 ] 
test_data2 = ["Ahmad", "Budi", "Charles", "Dodi", "Charles", "Eko", "Fajar", "Gugun", "Eko" ]
test_data3 = [ 0, 93, 76, 88, 29, 89, 30, 66, 27, 64, 59, 25, 71, 36, 65, 40, 39, 72, 43, 68, 83 ] 


#----------------------------------------------------------
"""
Code credit: 
https://stackoverflow.com/a/50883577
https://www.kite.com/python/answers/how-to-check-for-duplicates-in-a-list-in-python

Original code:

def contains_duplicates(X):
    return len(np.unique(X)) != len(X)
"""
def contains_duplicates(X):
	# print(X,"\n")
	# print(len(np.unique(X)))
	# print(len(X))
	return len(np.unique(X)) != len(X), len(X)-len(np.unique(X))

# anyDuplicate, dupNum = contains_duplicates(test_data1)
# print(anyDuplicate, dupNum)

#----------------------------------------------------------
"""
Code credit:
https://stackoverflow.com/a/51297779

Original code:

u, c = np.unique(a, return_counts=True)
dup = u[c > 1]
"""

def duplicated_data(dataMasuk):
	u, c = np.unique(dataMasuk, return_counts=True)
	# dup = u[c > 1]
	# dup.size
	return u[c > 1]

# print(duplicated_data(test_data1))

#----------------------------------------------------------

def test_fungsi_dup(dataFeed1):
	anyDuplicate, dupNum = contains_duplicates(dataFeed1)
	print(f"Benarkah ada data yang terduplikasi? {anyDuplicate}")
	if dupNum>0:
		print(f"Jumlah data yang terduplikasi? {dupNum}")
		print(f"Data yang terduplikasi adalah: {duplicated_data(dataFeed1)}")
	print("\n")
#----------------------------------------------------------


test_fungsi_dup(test_data1)



