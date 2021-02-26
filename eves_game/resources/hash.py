from collections import defaultdict
from pprint import pprint
from typing import List


class HashTable:
    def __init__(self, size: int) -> None:
        self.hash_table = defaultdict(list)
        self.max_size = size

    def generate_key(self, key: str) -> int:
        temp = [ord(i) for i in key]
        hash_key = sum(temp) % self.max_size
        return hash_key

    def add(self, key: str):
        if key in self.hash_table:
            raise Exception("Value already allotted to the slot !")

        hash_value = self.generate_key(key)
        self.hash_table[hash_value].append(key)
        return hash_value

    def get(self, key: str) -> List:
        if self.generate_key(key) not in self.hash_table:
            return None
        return self.hash_table[key]

    def delete(self, key: str) -> None:
        if self.generate_key(key) not in self.hash_table:
            raise Exception("Key not found !")
        del self.hash_table[self.generate_key(key)]

    def size(self) -> int:
        return len(self.hash_table.keys())

    def print_table(self):
        pprint(dict(self.hash_table))


