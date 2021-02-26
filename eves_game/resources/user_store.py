import pandas as pd

from eves_game.resources.hash import HashTable
from eves_game.visualizer import calculate_collision_probability


class UserStore:
    def __init__(self, hash_table: HashTable) -> None:
        self.users = {}
        self.hash_table = hash_table
        pass

    def add(self, user_id, password):
        print(
            f"Collision probability for {user_id}: {calculate_collision_probability(self.active_users_count(), self.hash_table.max_size)}")
        if user_id not in self.users:
            result = self.hash_table.add(password)
            self.users[user_id] = result['hash_value']
            if result['collision_status']:
                print(f"Collision status for {user_id}: {result['collision_status']}")
            return result['collision_status']
        else:
            raise Exception("User already exists !")

    def change_password(self, user_id, password):
        if user_id in self.users:
            self.users[user_id] = self.hash_table.add(password)
        else:
            raise Exception("User does not exist !")

    def authenticate(self, user_id, password):
        if self.users.get(user_id) is None:
            raise Exception("User does not exist !")
        return self.users[user_id] == self.hash_table.generate_key(password)

    def active_users_count(self):
        return len(self.users)

    def get_all_usernames(self):
        return self.users.keys()

    def get_all_users(self):
        print("\n-- Users --")
        print(pd.DataFrame.from_dict(dict(Username=self.users.keys(), HashValue=self.users.values()),
                                     orient='index').transpose())
