import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for seed in range(self.num_hashes):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def __contains__(self, item):
        for seed in range(self.num_hashes):
            index = mmh3.hash(item, seed) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

bf = BloomFilter(100, 5)
bf.add('apple')
bf.add('banana')

print('apple' in bf)
print('orange' in bf)

"""In this example, mmh3 is used to generate the hash functions, and bitarray is used to represent the bit array that holds the Bloom filter. The size parameter specifies the size of the bit array, and the num_hashes parameter specifies the number of hash functions to use. The add method adds an item to the Bloom filter, and the __contains__ method checks whether an item is in the Bloom filter.
"""

"""The in keyword is used to check if an element is a member of a collection. In the context of the Bloom filter example, print('apple' in bf) checks whether the string "apple" is a member of the Bloom filter bf.

The __contains__ method is implemented in the BloomFilter class to support the in keyword for checking membership. The __contains__ method uses the same hash functions as the add method to compute the indices in the bit array that correspond to the given item, and checks whether the bits at those indices are set to 1. If all the bits are set to 1, then the method returns True, indicating that the item is probably in the Bloom filter (with a small probability of a false positive). If any of the bits are set to 0, then the method returns False, indicating that the item is definitely not in the Bloom filter."""

"""https://stackoverflow.com/questions/2217001/override-pythons-in-operator"""