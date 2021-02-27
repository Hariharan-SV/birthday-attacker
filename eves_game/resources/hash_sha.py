from collections import defaultdict
from pprint import pprint
import hashlib 

class HashTable:
    def __init__(self) -> None:
        self.hash_table = defaultdict(list)

    def generate_key(self, key: str) -> int:
        hash_key = hashlib.sha256(key.encode())
        return hash_key.hexdigest()

    def add(self, key: str):

        hash_value = self.generate_key(key)
        collision = False

        if self.hash_table.get(hash_value):
            print(f"Hash Collision detected for hash value {hash_value}!")
            
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
