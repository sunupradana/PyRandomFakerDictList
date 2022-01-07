"""
Data generator untuk latihan. 

list, dictionary, array

https://replit.com/@sunupradana/Data-Generator-Latihan-01
"""

# import pandas as pd
import numpy as np
from faker import Faker
#from os import system

JUMLAHITERASI = 4

# dataz = np.array([ int() ])
#dataz = [ int() ]
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
# an_array = np.array(datarw)

print(datarw)
# print(an_array)
# an_array


