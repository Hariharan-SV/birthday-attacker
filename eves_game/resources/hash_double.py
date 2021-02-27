from collections import defaultdict
from pprint import pprint


class HashTable:
    def __init__(self, size: int) -> None:
        self.hash_table = defaultdict(list)
        self.max_size = size

    def generate_key(self, key: str, nounce=0) -> int:
        temp = [ord(i) for i in key]
        hash_key = (sum(temp) + nounce) % self.max_size
        return hash_key

    def double_table(self):
        temp_table = defaultdict(list)
        self.max_size = 2*self.max_size

        for values in self.hash_table.values():
            for value in values:
                key = self.generate_key(value)
                temp_table[key].append(value)
        self.hash_table = temp_table.copy()
        del temp_table

    def add(self, key: str):

        hash_value = self.generate_key(key)
        collision = False

        while self.hash_table.get(hash_value):
            print("Doubling Table !")
            print(f"Hash Collision detected for hash value {hash_value}!")
            self.double_table()
            hash_value = self.generate_key(key)

        self.hash_table[hash_value].append(key)
        return dict(hash_value=hash_value, collision_status=collision)

    def get(self, key: str):
        return self.hash_table.get(key)

    def delete(self, key: str) -> None:
        if self.generate_key(key) not in self.hash_table:
            raise Exception("Key not found !")
        del self.hash_table[self.generate_key(key)]

    def size(self) -> int:
        return len(self.hash_table.keys())

    def print_table(self):
        print("\n -- Hash Table --")
        pprint(dict(self.hash_table))
