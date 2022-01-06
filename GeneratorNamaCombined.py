"""
Combined first name and last name using array.
Nama unik/uniqe name
"""

from random import shuffle, seed
from faker.providers.person.en import Provider
import numpy as np

JUMLAH_NAMA = 200

first_names = list(set(Provider.first_names))
last_names = list(set(Provider.last_names))

# print(len(first_names))
# print(len(last_names))

# seed(4321)
shuffle(first_names)
shuffle(last_names)

# print(first_names[0:7])
# print(first_names[0:7)

#------------------
#Pembanding
nama = list(zip(first_names[0:JUMLAH_NAMA], last_names[0:JUMLAH_NAMA]))
print(nama,"\n")
print(nama[0])
print("\n")

li_nama = []

for inm in range(JUMLAH_NAMA):
    li_nama.append(first_names[inm]+" "+last_names[inm])

print(li_nama, "\n") 
#------------------

ar_nama = np.array([])

for inm in range(JUMLAH_NAMA):
    ar_nama = np.append(ar_nama, first_names[inm]+" "+last_names[inm])
    
print(ar_nama.reshape(JUMLAH_NAMA,1))
