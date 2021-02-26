import string
from random import randint, choices

import names
from colorama import init

from eves_game.resources.hash import HashTable
from eves_game.resources.user_store import UserStore
from eves_game.visualizer import visualize

init()


def perform_hacking(store: UserStore, hackers):
    for hacker in hackers:
        print(f"\nHacker={hacker['username']}")
        for user in store.get_all_usernames():
            if user != hacker['username']:
                status = store.authenticate(user, hacker['password'])
                if status:
                    print(f"\u001b[31m{user} - status: Hacked\u001b[39m")
                else:
                    print(f"\u001b[32m{user} - status: Hacking Failed :(\u001b[39m")


def simulate(table_size, number_of_users):
    table = HashTable(table_size)
    store = UserStore(table)
    hackers = []
    for _ in range(number_of_users):
        username = names.get_first_name() + ' ' + names.get_last_name()
        password = ''.join(choices(string.ascii_uppercase, k=randint(5, 6)))
        if store.add(username, password):
            hackers.append(dict(username=username, password=password))
        print()

    perform_hacking(store, hackers)
    store.get_all_users()
    store.hash_table.print_table()

    total_hacked = 0
    for i in store.hash_table.hash_table.values():
        if len(i) > 1:
            total_hacked += len(i)

    print(f"\n\u001b[31mTotal hacked: {total_hacked}\u001b[39m")

    visualize()


if __name__ == '__main__':
    simulate(10, 12)
