
"""
https://faker.readthedocs.io/en/master/index.html?highlight=names#unique-values

Generator nama unik sampai batas iterasi tertentu.

"""

import numpy as np

from faker import Faker
fake = Faker()
names = [fake.unique.first_name() for i in range(90)]
assert len(set(names)) == len(names)

print(names)


def duplicated_data(dataMasuk):
    # https://stackoverflow.com/a/51297779
    u, c = np.unique(dataMasuk, return_counts=True)
    # dup = u[c > 1]
    # print(dup.size)
    return u[c > 1]

print("\n")
print(duplicated_data(names))
print("\n")
