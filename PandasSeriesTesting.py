"""
Uji Pandas Series dengan data random hasil generator

"""

import pandas as pd
import numpy as np
from faker import Faker
#from os import system

JUMLAHITERASI = 8

# dataz = np.array([ int() ])
dataz = []

#namez = np.array([])
namez = []

fake = Faker()

# for idatz in range(JUMLAHITERASI):
#     dataz = np.append(dataz, np.random.randint(10,99))

for idatz in range(JUMLAHITERASI):
    dataz.append(np.random.randint(10,99))

# for idatz in range(JUMLAHITERASI):
#     namez = np.append(namez, fake.name())

for idatz in range(JUMLAHITERASI):
    namez.append(fake.name())

# print(dataz)
# print(namez)

mydict = dict(zip(namez,dataz))
print(mydict)
print("\n")

datarw = list(mydict.items())
an_array = np.array(datarw)
print(an_array)
print("\n")
# an_array
print(datarw)
print("\n")

print("---Pandas Series testing--- \n")

myds = pd.Series(mydict)
print(myds)


