from pprint import pprint
from eves_game.resources.hash import HashTable


class UserStore:
    def __init__(self, hash_table: HashTable) -> None:
        self.users = {}
        self.hash_table = hash_table
        pass

    def add(self, user_id, password):
        if user_id not in self.users:
            self.users[user_id] = self.hash_table.add(password)
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

    def get_all_users(self):
        pprint(self.users)


if __name__=="__main__":
    table = HashTable(4)
    store = UserStore(table)
    store.add("Harry","Programmer")
    store.add("Krish","KSGPSG")
    store.get_all_users()
    store.hash_table.print_table()