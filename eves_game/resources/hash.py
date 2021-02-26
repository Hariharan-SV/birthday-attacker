from collections import defaultdict
from typing import List


class HashTable:
    def __init__(self, size) -> None:
        self.data = defaultdict(List)
        self.max_size = size

    def generate_key(self, key: str) -> int:
        temp = [i for i in key]
        hash_key = sum(temp) % self.size
        return hash_key

    def add(self, key: str, value: str) -> None:
        if key in self.data:
            raise Exception("Value already alloted to the slot !")

        self.data[self.generate_key(key)].append(value)

        if self.max_size == self.size():
            self.max_size *= 2

    def get(self, key: str) -> List:
        if self.generate_key(key) not in self.data:
            return None
        return self.data[key]

    def delete(self, key: str) -> None:
        if self.generate_key(key) not in self.data:
            raise Exception("Key not found !")
        del self.data[self.generate_key(key)]

    def size(self) -> int:
        return len(self.data.keys())
    
    def print_data(self):
        print(self.data)
